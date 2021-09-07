import os

from tqdm import tqdm

project_path = r"C:\Users\user\Desktop\app\eryde\com.ubercab_v4.322.1"
http_file_rider = r"C:\Users\user\Desktop\app\eryde\http_file_rider_with_file.xml"

http_file = open(http_file_rider, 'w')
header_filename = False
writable_lines = []

for root, dirs, files in tqdm(os.walk(project_path, topdown=False)):
    for name in files:
        tmp_filepath = os.path.join(root, name)
        if header_filename:
            http_file.write("\n===============" + tmp_filepath + "\n")
            http_file.writelines(writable_lines)
            header_filename = False
            writable_lines = []
        try:
            with open(tmp_filepath, "r") as file:
                for line in file:
                    if 'https://' in line:
                        if not 'xmlns' in line:
                            header_filename = True
                            writable_lines.append(line)
                    elif 'http://' in line:
                        if not 'xmlns' in line:
                            header_filename = True
                            writable_lines.append(line)
        except UnicodeDecodeError as e:
            pass
        except Exception as  e:
            pass
http_file.close()
