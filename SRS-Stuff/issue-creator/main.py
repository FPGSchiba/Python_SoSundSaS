import json
import base64
import os
import re

from urllib.parse import unquote
from requests_toolbelt.multipart import decoder
import requests

TOKEN = os.getenv('TOKEN')


def get_key(form_data):
    # 'form-data; name="birth_date"', 'content': b'2012-123'
    key = form_data.split(";")[1].split("=")[1].replace('"', '')

    return key


def handler(event, context):
    headers = event['headers']
    postdata = base64.b64decode(event['body'])
    request = {}  # Save request here

    for part in decoder.MultipartDecoder(postdata, headers['Content-Type']).parts:
        content = part.content.decode('utf-8')
        content = unquote(content)
        parts = re.split(r'&(user|time)=', content, flags=re.MULTILINE)
        print(parts)
        request['log'] = parts[0].replace('log=', '').replace('+', ' ')
        request['user'] = parts[2]
        request['time'] = parts[4]
        print(request)
        print(content)

    body = f"""Crash Log:
```
{request['log']}
```

This is an automatic message and is only here so that the Development Team can work fast.
    """

    response = requests.post('https://api.github.com/repos/FPGSchiba/VNGD-SimpleRadioStandalone/issues', headers={
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {TOKEN}',
        'X-GitHub-Api-Version': '2022-11-28'
    },
                             json={
                                 'title': f'Crash by: {request["user"]} at {request["time"]}',
                                 'body': body,
                                 'labels': ['crash']
                             })

    if response.status_code == 201:
        return {
            'statusCode': 200,
            'body': response.json()['html_url']
        }
    return {
        'statusCode': response.status_code,
        'body': json.dumps(response.json()['state_reason'])
    }
