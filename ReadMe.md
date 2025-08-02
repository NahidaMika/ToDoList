# OUTDATED
# To Do List

A To Do List made in python using tkinter as a GUI.


## Screenshots

<img width="767" height="391" alt="image" src="https://github.com/user-attachments/assets/3fb64504-3bec-4123-b9fb-9aa225711cb2" />

> Main app

<img width="1920" height="928" alt="image" src="https://github.com/user-attachments/assets/b22f3ae9-6a7b-4181-8bdf-05bd66fc8685" />

> Web Editor

## Guide of Installation

- In the first execuion the program is going to create some files and directories that will be needed and the uses will have to manualy change such as the **Api-keys** and **FileID**.

- The current api for the json is [Json Bin](https://jsonbin.io/) that will be using the Api-key, the user will need to provide its own Api-key that is found in [Api-keys Json Bin](https://jsonbin.io/app/app/api-keys) and paste it in the file **_data/api-keys/JSONBINKEY_**.

- After placing the key in the file user must create a new json in [Json Bin Files](https://jsonbin.io/app/bins) placing this as its content **{"date": "yyyy-mm-dd",
  "todo": [{"task": "","status": "Not completed"}]}**.

- Then the user has to copy the **FileID** labeled as **_Bin Id_** and paste it in **_data/api-keys/FileID_**.

    - Then run again the program and everything should work as expected.



## Guide of Usage

As seen on the [Main app](#Screenshots) there are the **_Title_**, **_Last Updated_**, **_To Do List_** and some buttons.
Each button has its function:

- **Re-Download json** : Re-Downloads the json file to the directory **_data/json_**.

- **Reload json**: Reloads the content of the json onto the list.

- **Exit**: Closes the program and if **_Localhost_** is active it closes it.

- **Run LocalHost**: Launches the To-Do List Editor web. (can't be open twice)

- **Exit LocalHost**: Terminates the LocalHost.

In the [Web Editor](#Screenshots) there are some other elements to use:

- **Get json**: Get the json file to edit.

- **Update json**: Update the json in the textbox above.

- **Add Task**: Adds the written task to the textbox for later update.

## Authors

- [@NahidaMika](https://www.github.com/NahidaMika)

