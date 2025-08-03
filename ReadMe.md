# To Do List

A To Do List made in python using tkinter as a GUI.


## Screenshots

<img width="684" height="419" alt="image" src="https://github.com/user-attachments/assets/d7f41d98-4f32-4941-99cb-8e62b12fe06a" />

> Main app

<img width="1920" height="928" alt="image" src="https://github.com/user-attachments/assets/b22f3ae9-6a7b-4181-8bdf-05bd66fc8685" />

> Web Editor

<img width="683" height="448" alt="image" src="https://github.com/user-attachments/assets/e19812d2-29b2-4723-8baa-9813b879d807" />

> Editor

<img width="473" height="298" alt="image" src="https://github.com/user-attachments/assets/c4ce4fb9-4858-4896-8cb1-234f0e12249f" />

> Api-Keys editor

## Guide of Installation

- In the first execuion the program is going open a window called To-Do List Api-Key Editor where you can enter your own api-keys.

- The current api for the json is [Json Bin](https://jsonbin.io/) that will be using the Api-key, the user will need to provide its own Api-key that is found in [Api-keys Json Bin](https://jsonbin.io/app/app/api-keys).

- When the Api-key editor opens you can place the key and upload a template to create the json file.

- Then the user has to copy the FileID and paste it in.

- After the user places both the api-key and Fileid press the button Save & Exit.

## Guide of Usage

As seen on the [Api-key Editor Window](#Screenshots) there are some buttons.
Each button has its function:

- **Upload template** : It gets the provided api-key and upload a template.

- **Save** : Saves the provided api-key or FileId.

- **Save & Exit** : Saves the provided api-key or FileId and exits the window.

- **Exit** : Exits the window.

In the [Main app Window](#Screenshots):

- **Re-Download json** : Re-Downloads the json file to the directory **_data/json_**.

- **Reload json** : Reloads the content of the json onto the list.

- **Exit** : Closes the program and if **_Editor Window_** is active it closes it.

- **Open Editor** : Launches the To-Do List Editor.

In the [Editor Window](#Screenshots):

- **Re-Download json** : Re-Downloads the json file to the directory **_data/json_**.

- **Reload json** : Reloads the content of the json onto the list.

- **Exit** : Closes the program and if **_Localhost_** is active it closes it.

- **Run localhost** : Runs the Web Editor.

- **Exits localhost** : Closes the Web editor.

- **Update Status** : Updates the status of the selected task between _Completed_ and _Not Completed_.

- **Add Task** : Add the task entered in the textbox (Entry) with the status _Not Completed_.

- **Delete Task** : Delete the selected task from the json file.

- **Update Json** : Update the json in [Json Bin](https://jsonbin.io/app/bins).

- **Delete api-key** : Deletes the content of the file JSONBINKEY.

- **Delete FileID** : Deletes the content of the file FileID.

In the **_Web Editor_** there are some other elements to use:

- **Get json**: Get the json file to edit.

- **Update json**: Update the json in the textbox above.

- **Add Task**: Adds the written task to the textbox for later update.

## Authors

- [@NahidaMika](https://www.github.com/NahidaMika)

