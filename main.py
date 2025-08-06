import multiprocessing
import scripts.TkinterGUI as ToDoListGUI
from scripts.HTMLRequestsHandler import api_file_path

if __name__ == "__main__":
    multiprocessing.freeze_support()
    
    with open(api_file_path + 'JSONBINKEY', 'r') as file:
        key = file.read().strip()

    with open(api_file_path + 'FileID', 'r') as file:
        FileId = file.read().strip()
    
    if key == '' or FileId == '':
        ToDoListGUI.ApiKeyWindow()

    main = multiprocessing.Process(target=ToDoListGUI.mainWindow, args=())
    main.start()