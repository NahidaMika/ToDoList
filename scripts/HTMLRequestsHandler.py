import json
import os
import requests
from pathlib import Path, PureWindowsPath

#File paths
json_file_path_windows = PureWindowsPath('data\\json\\a')
json_file_path_not_final = str(Path(json_file_path_windows))
json_file_path = json_file_path_not_final[:-1]

id_file_path_windows = PureWindowsPath('data\\id\\a')
id_file_path_not_final = str(Path(id_file_path_windows))
id_file_path = id_file_path_not_final[:-1]

api_file_path_windows = PureWindowsPath('data\\api-keys\\a')
api_file_path_not_final = str(Path(api_file_path_windows))
api_file_path = api_file_path_not_final[:-1]

def check_for_necesary_paths():
    if not os.path.exists(json_file_path):
        os.makedirs(json_file_path)
        print(f'Path "{json_file_path}" created')
    else:
        print(f'Path "{json_file_path}" already exists')

    if not os.path.exists(api_file_path):
        os.makedirs(api_file_path)
        print(f'Path "{api_file_path}" created')
    else:
        print(f'Path "{api_file_path}" already exists')

def check_for_necesary_files():
    if not os.path.exists(json_file_path + 'ToDoList.json'):
        with open(json_file_path + 'ToDoList.json', 'xt') as json_file:
            json_file.write({"date":"","todo":[{"task":"","status":"Not completed"}]})
        print('File "ToDoList.json" created')
    else:
        print('File "ToDoList.json" already exists')
        pass

    if not os.path.exists(api_file_path + 'JSONBINKEY'):
        with open(api_file_path + 'JSONBINKEY', 'xt'):
            pass
        print('File "JSONBINKEY" created')
    else:
        print('File "JSONBINKEY" already exists')
        pass
    
    if not os.path.exists(api_file_path+ 'FileID'):
        with open(api_file_path + 'FileID', 'xt'):
            pass
        print('File "FileID" created')
    else:
        print('File "FileID" already exists')
        pass

#API keys
try:
    JsonBinApiKey = open(api_file_path + 'JSONBINKEY', 'r')
    JsonBinApiKey = JsonBinApiKey.read()

    # JSONHOSTKEY = open(api_file_path + 'JSONHOSTKEY', 'r')
    # JSONHOSTKEY = JSONHOSTKEY.read()

except FileNotFoundError as e:
    print('Error:', e)
    check_for_necesary_paths()
    check_for_necesary_files()

try:
    key = JsonBinApiKey.strip()

except NameError as e:
    print('Error:', e)
    key = ''

get_file_id_from_file = open(api_file_path + 'FileID', 'r')
get_file_id_from_file = get_file_id_from_file.read()
FileId = get_file_id_from_file.strip()

def check_json():
    try:
        os.rename(json_file_path + f'ToDoList.json', json_file_path + f'ToDoList.json.old')
    except FileExistsError:
        os.remove(json_file_path + f'ToDoList.json.old')
        os.rename(json_file_path + f'ToDoList.json', json_file_path + f'ToDoList.json.old')
    except FileNotFoundError:
        pass

def json_backup_checker(): # Checks if there is a json file and renames it and move it to the backup folder
    try:
        os.rename(json_file_path + f'ToDoList.json', json_file_path + f'ToDoList.json.backup')
    except FileExistsError:
        os.remove(json_file_path + f'ToDoList.json.backup')
        os.rename(json_file_path + f'ToDoList.json', json_file_path + f'ToDoList.json.backup')
    except FileNotFoundError:
        pass

def save_backup_jsonbin(data):
    json_backup_checker()
    with open(json_file_path + 'ToDoList.json', 'xt') as json_file:
        json.dump(data, json_file)

def upload_jsonbin(jsondata): #May never be in use
    url = f'https://api.jsonbin.io/v3/b/{FileId}'
    headers = {
    'Content-Type': 'application/json',
    'X-Master-Key': key, 
    }

    req = requests.request("PUT", url, json=jsondata, headers=headers)

    if req.status_code == 200:
        print('File uploaded successfully')
    else:
        print(req.status_code, req.reason)
        print('Failed to upload file')

def download_jsonbin():
    url = f'https://api.jsonbin.io/v3/b/{FileId}'
    headers = {
    'X-Master-Key': key.strip(),
    'X-Bin-Meta': 'false'
    }

    req = requests.get(url, json=None, headers=headers)

    if req.status_code == 200:
        check_json()
        with open(json_file_path + 'ToDoList.json', 'wb') as file:
            file.write(req.content)
        print('File downloaded successfully')

    else:
        print(req.status_code, req.reason)
        print('Failed to download file')

def load_jsonbin(): #May never be in use
    try:
        json_path = open(json_file_path + 'ToDoList.json', 'r')
        json_data = json.load(json_path)
        json_path.close()

        return json_data
    
    except FileNotFoundError:
        print('File not found\n' \
        'Please download the file')

if __name__ == '__main__':
    #download_jsonbin()
    #check_for_necesary_files()
    pass