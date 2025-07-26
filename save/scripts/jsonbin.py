import time
import datetime
import json
import os
import sys
from pathlib import Path, PureWindowsPath

if __name__ == '__main__':
    from jsonmaker import JSONBINKEY, data, url,id_file_path, json_file_path, check_json, api_file_path
elif __name__ == 'jsonbin':
    from jsonmaker import JSONBINKEY, data, url,id_file_path, json_file_path, check_json, api_file_path
else:
    from scripts.jsonmaker import JSONBINKEY, data, url,id_file_path, json_file_path, check_json, api_file_path

import requests

key = JSONBINKEY.strip()
get_file_id_from_file = open(api_file_path + 'FileID', 'r')
get_file_id_from_file = get_file_id_from_file.read()
json_file_id = get_file_id_from_file.strip()

def upload_json2(): #May never be in use
    headers = {
    'Content-Type': 'application/json',
    'X-Master-Key': key, 
    'X-Bin-Name': 'ToDoList',
    'X-Bin-Private': 'false'
    }

    req = requests.request("POST", url, json=data, headers=headers)

    if req.status_code == 200:
        print('File uploaded successfully')

    id = req.text

    with open(id_file_path + 'id.json', 'w') as file:
        file.write(id)

def download_jsonbin():
    url = f'https://api.jsonbin.io/v3/b/{json_file_id}'
    headers = {
    'X-Master-Key': key.strip()
    }

    req = requests.get(url, json=None, headers=headers)
    #print(req.text)

    #print(req.status_code)

    if req.status_code == 200:
        check_json()
        with open(json_file_path + 'ToDoList.json', 'wb') as file:
            file.write(req.content)
        print('File downloaded successfully')

    else:
        print('Failed to download file')
        exit()

def load_jsonbin(): #May never be in use
    try:
        json_path = open(json_file_path + 'ToDoList.json', 'r')
        json_data = json.load(json_path)
        json_path.close()

        return json_data
    
    except FileNotFoundError:
        print('File not found\n' \
        'Please download the file')
        exit()

if __name__ == '__main__':
    #download_jsonbin()
    load_jsonbin()
    

# test = {'record': 
#         {'date': '2222-22-22', 
#         'todo': [
#             {'task': 'Decirle a ', 'status': 'Not completed'},
#             {'task': 'Modify json with a checkbar', 'status': 'Not completed'}, 
#             {'task': 'Reload json while active', 'status': 'Not completed'}, 
#             {'task': 'Check http json maker', 'status': 'Not completed'}, 
#             {'task': 'Finish to-do list app', 'status': 'Not completed'}]}, 
#         'metadata': {
#             'id': '686490938a456b7966b9cc45', 
#             'private': True, ''
#             'createdAt': '2025-07-02T01:51:15.899Z', ''
#             'name': 'ToDoList'}}

# print(test['record']['date'])
# print(test['record']['todo'])

# for i in range(len(test['record']['todo'])):
#     print(test['record']['todo'][i]['task'])
#     print(test['record']['todo'][i]['status'])

# print(test['metadata']['id'])
# print(test['metadata']['private'])
# print(test['metadata']['createdAt'].replace('T', '/').replace('Z', '').split('/')[0])
# print(test['metadata']['name'])
