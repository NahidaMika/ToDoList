import scripts.TktinterGUI as ToDoListGUI
from scripts.jsonmaker import check_for_necesary_files

import multiprocessing

if __name__ == "__main__":
    multiprocessing.freeze_support()

    check_for_necesary_files()

    t = multiprocessing.Process(target=ToDoListGUI.mainWindow, args=())
    t.start()