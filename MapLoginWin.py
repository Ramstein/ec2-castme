import logging
import os
import shutil
from datetime import datetime, timezone

import boto3
import botocore
from botocore.exceptions import ClientError


region_name = 'ap-south-1'
aws_access_key_id = "budf"   # quarantined
aws_secret_access_key = "5T5hdaugbauyd"  # quarantined
CharacterMeshUpload_Not_Preprocessed = 'CharacterMeshUpload_Not_Preprocessed'
CharacterMeshUpload_Sucess_Preprocessed = 'CharacterMeshUpload_Sucess_Preprocessed'
ChracterMeshFromWeb_s3 = 'character-mesh-from-web'
CharacterMeshPreprocessed_s3 = "character-mesh-preprocessed"

local_fbx_download_dir = r'C:\Users\user\Downloads'
project_skeletal_mesh_import_dir = r"C:\Users\user\Documents\Unreal Projects\PythonTest\Content\SkeletalMesh"
skeleton_path = "/Game/Mesh/Girl/Jody_Skeleton.Jody_Skeleton"
SkeletalMeshFolderInUE4 = "/Game/SkeletalMesh"

dynamo_table = boto3.resource('dynamodb',
                              region_name=region_name,
                              aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key,
                              ).Table(CharacterMeshUpload_Not_Preprocessed)
dynamodb_cli = boto3.client('dynamodb',
                            region_name=region_name,
                            aws_access_key_id=aws_access_key_id,
                            aws_secret_access_key=aws_secret_access_key)

s3_client = boto3.client('s3',
                         region_name=region_name,
                         aws_access_key_id=aws_access_key_id,
                         aws_secret_access_key=aws_secret_access_key)



def fetch_from_CharacterMeshUpload_Not_Preprocessed():
    result = []
    try:
        result = dynamo_table.scan()
    except Exception as e:
        print(e)
    if result:
        return result["Items"]
    else:
        return result


def delete_from_CharacterMeshUpload_Not_Preprocessed_and_append_in_CharacterMeshUpload_Sucess_Preprocessed(Items):
    # deleting item from the table
    with dynamo_table.batch_writer() as batch:
        i = 0
        for item in Items:
            now_time = datetime.now(tz=timezone.utc).strftime('%y-%m-%d %H:%M:%S')
            try:
                batch.delete_item(Key={'filename': item['filename'], 'UploadTime': item["UploadTime"]})
                i += 1
                if i == 5:
                    break
                res = dynamodb_cli.put_item(TableName=CharacterMeshUpload_Sucess_Preprocessed,
                                            Item={
                                                'filename': {'S': item['filename']},
                                                'ID': {'N': item['ID']},
                                                'user_email': {'S': item['user_email']},
                                                'display_name': {'S': item['display_name']},
                                                'UploadTime': {'S': item["UploadTime"]},
                                                'PreprocessedTime': {'S': str(now_time)},
                                            })
            except Exception as e:
                print(e)



def download_dir(prefix, local, bucket=CharacterMeshPreprocessed_s3, client=s3_client):
    """
    params:
    - prefix: pattern to match in s3
    - local: local path to folder in which to place files
    - bucket: s3 bucket with target contents
    - client: initialized s3 client object
    """
    keys = []
    dirs = []
    next_token = ''
    base_kwargs = {
        'Bucket': bucket,
        'Prefix': prefix,
    }
    while next_token is not None:
        kwargs = base_kwargs.copy()
        if next_token != '':
            kwargs.update({'ContinuationToken': next_token})
        results = client.list_objects_v2(**kwargs)
        contents = results.get('Contents')
        for i in contents:
            k = i.get('Key')
            if k[-1] != '/':
                keys.append(k)
            else:
                dirs.append(k)
        next_token = results.get('NextContinuationToken')
    for d in dirs:
        dest_pathname = os.path.join(local, d)
        if not os.path.exists(os.path.dirname(dest_pathname)):
            os.makedirs(os.path.dirname(dest_pathname))
    for k in keys:
        dest_pathname = os.path.join(local, k)
        if not os.path.exists(os.path.dirname(dest_pathname)):
            os.makedirs(os.path.dirname(dest_pathname))
        try:
            print("Downloading {}".format(dest_pathname))
            client.download_file(bucket, k, dest_pathname)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
            else:
                raise


def main():
    Items = fetch_from_CharacterMeshUpload_Not_Preprocessed()
    for item in Items:
        '''Downloading skeletal mesh'''
        download_mesh(s3_filename=item['filename'], local_dir=local_fbx_download_dir)

        '''Run import script and wait for completion, run more scripts for fine tuning'''
        fbx_file = os.path.join(local_fbx_download_dir, item['filename'])
        destination_path = SkeletalMeshFolderInUE4 + "/" + item["ID"]
        imported_asset_path = import_mesh(skeleton_path, fbx_file, destination_path, destination_name=item["ID"])

        '''Uploading completely fine tuned character to s3 as a complete folder'''
        upload_dir_to_s3(ID=item['ID'])

        '''Deleting local .fbx file, imported folder in UE4 and from CharacterMeshPreprocessed_s3 bucket'''
        try:
            if os.path.exists(fbx_file):
                os.remove(fbx_file)
            else:
                print("The file does not exist, or have already got deleted.")
        except Exception as e:
            print(e)

        try:
            # Removes the specified directory, all subdirectories, and all files.
            shutil.rmtree(os.path.join(project_skeletal_mesh_import_dir, item['ID']))
        except Exception as e:
            print(e)
        delete_mesh(s3_filename=item['filename'])

    # updating both of the dynamodb tables
    delete_from_CharacterMeshUpload_Not_Preprocessed_and_append_in_CharacterMeshUpload_Sucess_Preprocessed(Items=Items)




# # os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
# print("Run the command but check that Chrome opened or not.")
#
# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()
#
# # open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())
# f.close()
#
# # importing os module
# import os
#
# # Directory
# directory = "GeeksforGeeks"
#
# # Parent Directory path
# parent_dir = "C:/Users/Administrator/Desktop/"
#
# # Path
# path = os.path.join(parent_dir, directory)
#
# # Create the directory
# # 'GeeksForGeeks' in
# # '/home / User / Documents'
# # os.mkdir(path)
# print("Directory '% s' created" % directory)
#
# # Directory
# directory = "Geeks"
#
# # Parent Directory path
# parent_dir = "C:/Users/Administrator/Desktop"
#
# # mode
# mode = 0o666
#
# # Path
# path = os.path.join(parent_dir, directory)
#
# # Create the directory
# # 'GeeksForGeeks' in
# # '/home / User / Documents'
# # with mode 0o666
# # os.mkdir(path, mode)
# print("Directory '% s' created" % directory)
#
# # os.rename("C:/Users/Administrator/Desktop/demofile2.txt", "C:/Users/Administrator/Desktop/GeeksforGeeks/file.txt")
#
#
# original = r"C:/Kirara"
# target = r"C:/ne"
#
# # shutil.move(original,target)

# exec('AssetFunctions.py')
# import os
# os.system('python AssetFunctions.py')


#!/usr/bin/python2.7
print("Run the command.")
i=1
while(i):
    if i==5000:
        break
    i+=1
    print(i)

#!/usr/bin/python3.7
print("hello from python 3.4")