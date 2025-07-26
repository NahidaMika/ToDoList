import datetime
import json
import os

import requests
from pathlib import Path, PureWindowsPath

#test data
data = {
    'date': datetime.datetime.now().strftime('%Y-%m-%d'),
    'todo': [
        {'task': 'Decirle a Cami', 'status': 'Not completed'},
        {'task': 'Modify json with a checkbar', 'status': 'Not completed'},
        {'task': 'Reload json while active', 'status': 'Not completed'},
        {'task': 'Check http json maker', 'status': 'Not completed'},
        {'task': 'Finish to-do list app', 'status': 'Not completed'}
    ]
}

date = data['date']
todo = data['todo']

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

#URL
url = 'https://api.jsonbin.io/v3/b'

def check_for_necesary_paths():
    for i in range(5):
        if not os.path.exists(json_file_path):
            os.makedirs(json_file_path)
        else:
            print('Path "json" already exists')

        if not os.path.exists(api_file_path):
            os.makedirs(api_file_path)
        else:
            print('Path "api-keys" already exists')

        break

def check_for_necesary_files():
    for i in range(5):
        if not os.path.exists(json_file_path + 'ToDoList.json'):
            with open(json_file_path + 'ToDoList.json', 'xt'):
                pass
        else:
            print('File "ToDoList.json" already exists')
            pass

        if not os.path.exists(api_file_path + 'JSONBINKEY'):
            with open(api_file_path + 'JSONBINKEY', 'xt'):
                pass
        else:
            print('File "JSONBINKEY" already exists')
            pass

        if not os.path.exists(api_file_path + 'JSONHOSTKEY'):
            with open(api_file_path + 'JSONHOSTKEY', 'xt'):
                pass
        else:
            print('File "JSONHOSTKEY" already exists')
            pass
        
        if not os.path.exists(api_file_path+ 'FileID'):
            with open(api_file_path + 'FileID', 'xt'):
                pass
        else:
            print('File "FileID" already exists')
            pass

        break


#API keys
try:
    JSONBINKEY = open(api_file_path + 'JSONBINKEY', 'r')
    JSONBINKEY = JSONBINKEY.read()

    JSONHOSTKEY = open(api_file_path + 'JSONHOSTKEY', 'r')
    JSONHOSTKEY = JSONHOSTKEY.read()

except FileNotFoundError:
    for i in range(5):
        print('Files not found')
        check_for_necesary_paths()
        check_for_necesary_files()
        break

def check_json():
    try:
        os.rename(json_file_path + f'ToDoList.json', json_file_path + f'ToDoList.json.old')
    except FileExistsError:
        os.remove(json_file_path + f'ToDoList.json.old')
        os.rename(json_file_path + f'ToDoList.json', json_file_path + f'ToDoList.json.old')
    except FileNotFoundError:
        pass

def make_json():
    check_json()
    
    # Serializing json
    json_loc = open(json_file_path + 'ToDoList.json', 'xt')
    json_object = json.dump({'date': date, 'todo': todo}, json_loc)
    json_loc.close()

    return json_object

def upload_json():
    POST_json =requests.request('POST', 'https://jsonhost.com/json/DemoJsonAPIEndpointForDemoReason', files={'upload_file': open(json_file_path + 'ToDoList.json', 'rb')}, headers={'Authorization': JSONHOSTKEY})
    print(POST_json.status_code)
    print(POST_json.text)

def download_json():
    check_json()

    GET_json = requests.request('GET', f'{url}/ToDoList.json')
    
    if GET_json.status_code == 200:
        check_json()
        with open(json_file_path + 'ToDoList.json', 'wb') as file:
            file.write(GET_json.content)
        print('File downloaded successfully')

    else:
        print('Failed to download file')
        exit()
    
def load_json():
    try:
        json_path = open(json_file_path + f'ToDoList.json', 'r')
        json_data = json.load(json_path)
        json_path.close()

        json_date = json_data['date']
        json_todo = json_data['todo']

        for i in range(len(json_todo)):
            print(json_todo[i]['task'])
            print(json_todo[i]['status'])

        return json_data
    
    except FileNotFoundError:
        print('File not found\n' \
        'Please download the file')
        exit()

if __name__ == '__main__':
    pass