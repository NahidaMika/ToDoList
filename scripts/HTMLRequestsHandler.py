import json
import os
import requests
from pathlib import Path, PureWindowsPath
import webbrowser
from time import sleep

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

def check_for_necesary_paths(): #Check if the path for files exist
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

def check_for_necesary_files(): #Check if the files exist
    if not os.path.exists(json_file_path + 'ToDoList.json'):
        with open(json_file_path + 'ToDoList.json', 'xt') as json_file:
            json.dump({"date":"","todo":[{"task":"","status":"Not completed"}]}, json_file)
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

def jsonbin_io_main(): # Opens jsonbin.io
    webbrowser.open('https://jsonbin.io/')

def jsonbin_io_bins(): # Opens jsonbin.io Bins
    webbrowser.open('https://jsonbin.io/app/bins')

def check_json(): # Checks if there is a json file and renames it
    try:
        os.rename(json_file_path + f'ToDoList.json', json_file_path + f'ToDoList.json.old')
    except FileExistsError:
        os.remove(json_file_path + f'ToDoList.json.old')
        os.rename(json_file_path + f'ToDoList.json', json_file_path + f'ToDoList.json.old')
    except FileNotFoundError:
        pass

def json_backup_checker(): # Checks if there is a json file and renames it 
    try:
        os.rename(json_file_path + f'ToDoList.json', json_file_path + f'ToDoList.json.backup')
    except FileExistsError:
        os.remove(json_file_path + f'ToDoList.json.backup')
        os.rename(json_file_path + f'ToDoList.json', json_file_path + f'ToDoList.json.backup')
    except FileNotFoundError:
        pass

def save_backup_jsonbin(data): #Saves the json file backup
    json_backup_checker()
    with open(json_file_path + 'ToDoList.json', 'xt') as json_file:
        json.dump(data, json_file)

def upload_jsonbin(jsondata): # Uploads the json file
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

def load_jsonbin(): # Loads the json file contents
    try:
        json_path = open(json_file_path + 'ToDoList.json', 'r')
        json_data = json.load(json_path)
        json_path.close()

        return json_data
    
    except FileNotFoundError:
        print('File not found\n' \
        'Please download the file')

def download_jsonbin(): # Downloads the json file contents
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



def make_jsonbin(jsondata, apikey): # Uploads a new json file
    url = 'https://api.jsonbin.io/v3/b'
    headers = {
    'Content-Type': 'application/json',
    'X-Master-Key': apikey, 
    }

    req = requests.request("POST", url, json=jsondata, headers=headers)

    if req.status_code == 200:
        print('File uploaded successfully')
    else:
        print(req.status_code, req.reason)
        print('Failed to upload file')

    return req

def meow_facts(count: int = 1) -> dict: # Gets meow facts
    meow_facts_dict = {}
    url = f'https://meowfacts.herokuapp.com/?count={count}' #&lang={lang}

    req = requests.request("GET", url)

    if req.status_code == 200:
            meow_facts = req.text
            meow_facts = json.loads(meow_facts)
            meow_facts_dict = meow_facts

            return meow_facts_dict

    else:
        print(req.status_code, req.reason)
        print('Failed to get facts')

    return meow_facts_dict

def get_meow_facts(timeout: int = 300, count: int = 0): # Gets meow facts
    while True:
        fact = meow_facts()
        print(fact['data'][count])
        sleep(timeout)

if __name__ == '__main__':
    #download_jsonbin()
    #check_for_necesary_files()
    #meow_facts(100)
    pass