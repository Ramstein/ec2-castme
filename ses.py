import boto3


## Creating email tempaltes

ses = boto3.client('ses')

# Template = ses.create_template(
#         Template:{
#         'TemplateName':'Hello',
#         'SubjectPart': "Welcome ON BOard",
#         'TextPart': 'Thanks a lot for watching it',
#         'HtmlPart': 'Thanks a lot for watching it',
#         }
#     )

ses.get_template(TemplateName = 'Hello')
ses.list_templates()

## send emails
ses.send_templated_email(
    Source = "support@castme.life",
    Destination= {
        'ToAddress': ['gerialworld@gmail.com', 'rodrixx.3112@gamil.com'],
        'CcAddress': ['gerialworld@gmail.com', 'rodrixx.3112@gamil.com'],
    },
    ReplyToAddresses = ['support@castme.life',],
    Template = 'Hello',
    TemplateData = '{"replace tag name": "with value"}'
)


body = """
    This is your body message
"""

ses.send_email(
    Source="support@castme.life",
    Destination={
        'ToAddress': ['gerialworld@gmail.com', 'rodrixx.3112@gamil.com'],
        'CcAddress': ['gerialworld@gmail.com', 'rodrixx.3112@gamil.com'],
    },
    ReplyToAddresses=['support@castme.life', ],
    Message = {
        'Subject':{
            'Data': 'You can pass your subject here',
            'Charset': 'utf-8'
        },
        'Body':{
            'Text':{
                'Data': '',
                'Charset': 'utf-8'
            },
            'Html':{
                'Data': 'This is your body message in html',
                'Charset': 'utf-8'
            }
        }
    }
)