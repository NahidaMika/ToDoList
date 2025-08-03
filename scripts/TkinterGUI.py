from tkinter import *
from tkinter import ttk

import os
import multiprocessing
import time
import datetime
import json

if __name__ == '__main__':
    from HTMLRequestsHandler import load_jsonbin, download_jsonbin, save_backup_jsonbin, upload_jsonbin, api_file_path, make_jsonbin, jsonbin_io_main, jsonbin_io_bins
    import localhostHTML as LocalHost
else:
    from scripts.HTMLRequestsHandler import load_jsonbin, download_jsonbin, save_backup_jsonbin, upload_jsonbin, api_file_path, make_jsonbin, jsonbin_io_main, jsonbin_io_bins
    import scripts.localhostHTML as LocalHost


class ToDoListGUI:
    def __init__(self, root):
        self.root = root
        self.user = self.get_user()
        self.root.title(f"{self.user}'s To-Do List")
        self.root.resizable(False, False)

        self.editor = multiprocessing.Process(target=editorWindow, args=())

        try:
            icon = PhotoImage(file="icon.ico")
            # small_icon = PhotoImage(file="icon-16.png")
            # big_icon = PhotoImage(file="icon-32.png")
            # root.iconphoto(False, big_icon, small_icon)
            root.iconphoto(True, icon)
        except TclError:
            print("Error: Icon could not be loaded. Make sure 'icon.ico' exists and is in the correct path.")
        except FileNotFoundError:
            print("Error: File 'icon.ico' not found.")
        except Exception as e:
            print(f"Unexpected error: {e}")

        try:
            self.data = load_jsonbin()
            self.json_data = self.data
            self.json_date = self.data
        except json.decoder.JSONDecodeError:
            self.json_date = {"date": datetime.datetime.now().strftime('%Y-%m-%d')}
            self.json_data = {"todo": [{"task": "", "status": ""}]}

        self.mainframe = ttk.Frame(self.root)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        for i in range(5):
            self.root.columnconfigure(i, weight=1)
            self.root.rowconfigure(i, weight=1)

        self.lastupdate = ttk.Frame(self.mainframe)
        self.lastupdate.grid(column=0, row=1, sticky=N+S+W+E)
        for i in range(5):
            self.lastupdate.columnconfigure(i, weight=1)
            self.lastupdate.rowconfigure(i, weight=1)

        ttk.Label(self.mainframe, text=f"{self.user}'s To-Do List", font=("Arial", 16, "bold", "underline")).grid(column=0, row=0, sticky=W)

        self.todo_date_var = StringVar()
        self.todo_date_var.set(self.json_date['date'])

        ttk.Label(self.lastupdate, text=f"Last update:", font=("Arial", 12, "bold")).grid(column=0, row=0, sticky=E)
        ttk.Label(self.lastupdate, textvariable=self.todo_date_var, font=("Arial", 12)).grid(column=1, row=0, sticky=W)

        self.treeview_frame = ttk.Frame(self.mainframe)
        self.treeview_frame.grid(column=0, row=2, sticky=N+S+W+E)
        for i in range(5):
            self.treeview_frame.columnconfigure(i, weight=1)
            self.treeview_frame.rowconfigure(i, weight=1)

        self.button_frame = ttk.Frame(self.mainframe)
        self.button_frame.grid(column=0, row=3, sticky=N+S+W+E)
        for i in range(5):
            self.button_frame.columnconfigure(i, weight=1)
            self.button_frame.rowconfigure(i, weight=1)

        self.treeview = ttk.Treeview(self.treeview_frame, columns=('todo', 'status'))
        self.treeview.grid(column=1, row=2, sticky=N+S+W)

        self.treeview.column("#0", width=0, stretch=NO)
        self.treeview.column("todo", anchor=W, width=300)
        self.treeview.column("status", anchor=W, width=100)

        self.treeview.heading("#0", text="", anchor=W)
        self.treeview.heading("todo", text="To-Do", anchor=W)
        self.treeview.heading("status", text="Status", anchor=W)

        self.todo_task_var = StringVar()
        self.todo_status_var = StringVar()

        for i, todo in enumerate(self.json_data['todo']):
            self.todo_task_var.set(todo['task'])
            self.todo_status_var.set(todo['status'])
            self.treeview.insert('', 'end', values=(self.todo_task_var.get(), self.todo_status_var.get()))

        ttk.Button(self.button_frame, text=f"Re-Download json", command=self.download_todo_json).grid(column=1, row=3, sticky=W)
        ttk.Button(self.button_frame, text=f"Reload json", command=self.get_json_data).grid(column=2, row=3, sticky=W)
        ttk.Button(self.button_frame, text=f"Exit", command=self.exit).grid(column=3, row=3, sticky=W)
        ttk.Button(self.button_frame, text=f"Open Editor", command=self.open_editor).grid(column=4, row=3, sticky=W)        

        for child in self.mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        for child in self.button_frame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        for child in self.treeview_frame.winfo_children(): 
            child.grid_configure(padx=30, pady=5)

        for child in self.lastupdate.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

    def get_json_data(self): # Reloads the json file on the GUI
        try:
            self.json_data = load_jsonbin()

            self.json_date = self.json_data
            self.json_data = self.json_data

            self.todo_date_var.set(self.json_date['date'])
            self.treeview.delete(*self.treeview.get_children())
            for i, todo in enumerate(self.json_data['todo']):
                self.todo_task_var.set(todo['task'])
                self.todo_status_var.set(todo['status'])
                self.treeview.insert('', 'end', values=(self.todo_task_var.get(), self.todo_status_var.get()))

            print("Json reloaded")

        except json.decoder.JSONDecodeError as e:
            print('Error:', e)
        
    def get_user(self): # Gets the current user's name
        cdw = os.getcwd()
        if cdw.startswith("/") == True:
            cdw = cdw.split("/")
            user = cdw[2]
            user = user.capitalize()
            return user
        
        else :
            cdw = cdw.split("\\")
            user = cdw[2]
            user = user.capitalize()
            return user

    def download_todo_json(self): # Re-Download the json file
        download_jsonbin()
        self.get_json_data()

    def open_editor(self):
        self.editor = multiprocessing.Process(target=editorWindow, args=())
        self.editor.start()

    def exit(self): # Exits the program
        print("Exiting the program...")
        time.sleep(2)
        if self.editor.is_alive() == True:
            self.editor.terminate() #Only with multiprocessing
            # self.p2.join() #Only with threading
        else :
            print('Editor is closed')
        self.root.destroy()

    def run(self): # Runs the GUI
        self.root.mainloop()

class ToDoListEditor(ToDoListGUI):
    def __init__(self, root):
        self.root = root
        self.user = self.get_user()
        self.root.title(f"{self.user}'s To-Do List Editor")
        #self.root.resizable(False, False)

        self.p2 = multiprocessing.Process(target=LocalHost.runlocalhost, args=("0.0.0.0", 5000)) #Only with multiprocessing

        # self.p2 = threading.Thread(target=LocalHost.runlocalhost, args=()) #Only with threading

        try:
            icon = PhotoImage(file="icon.ico")
            # small_icon = PhotoImage(file="icon-16.png")
            # big_icon = PhotoImage(file="icon-32.png")
            # root.iconphoto(False, big_icon, small_icon)
            root.iconphoto(True, icon)
        except TclError:
            print("Error: Icon could not be loaded. Make sure 'icon.ico' exists and is in the correct path.")
        except FileNotFoundError:
            print("Error: File 'icon.ico' not found.")
        except Exception as e:
            print(f"Unexpected error: {e}")

        try:
            self.data = load_jsonbin()
            self.json_data = self.data
            self.json_date = self.data
        except json.decoder.JSONDecodeError:
            self.json_date = {"date": datetime.datetime.now().strftime('%Y-%m-%d')}
            self.json_data = {"todo": [{"task": "", "status": ""}]}

        self.mainframe = ttk.Frame(self.root)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        for i in range(5):
            self.root.columnconfigure(i, weight=1)
            self.root.rowconfigure(i, weight=1)

        self.lastupdate = ttk.Frame(self.mainframe)
        self.lastupdate.grid(column=0, row=1, sticky=N+S+W+E)
        for i in range(5):
            self.lastupdate.columnconfigure(i, weight=1)
            self.lastupdate.rowconfigure(i, weight=1)

        ttk.Label(self.mainframe, text=f"{self.user}'s To-Do List Editor", font=("Arial", 16, "bold", "underline")).grid(column=0, row=0, sticky=W)

        self.todo_date_var = StringVar()
        self.todo_date_var.set(self.json_date['date'])

        ttk.Label(self.lastupdate, text=f"Last update:", font=("Arial", 12, "bold")).grid(column=0, row=0, sticky=E)
        ttk.Label(self.lastupdate, textvariable=self.todo_date_var, font=("Arial", 12)).grid(column=1, row=0, sticky=W)

        self.treeview_frame = ttk.Frame(self.mainframe)
        self.treeview_frame.grid(column=0, row=2, sticky=N+S+W+E)
        for i in range(5):
            self.treeview_frame.columnconfigure(i, weight=1)
            self.treeview_frame.rowconfigure(i, weight=1)

        self.button_frame = ttk.Frame(self.mainframe)
        self.button_frame.grid(column=0, row=3, sticky=N+S+W+E)
        for i in range(5):
            self.button_frame.columnconfigure(i, weight=1)
            self.button_frame.rowconfigure(i, weight=1)

        self.treeview = ttk.Treeview(self.treeview_frame, columns=('todo', 'status'))
        self.treeview.grid(column=0, row=2, sticky=N+S+W)

        self.treeview.column("#0", width=0, stretch=NO)
        self.treeview.column("todo", anchor=W, width=300)
        self.treeview.column("status", anchor=W, width=100)

        self.treeview.heading("#0", text="", anchor=W)
        self.treeview.heading("todo", text="To-Do", anchor=W)
        self.treeview.heading("status", text="Status", anchor=W)

        self.todo_task_var = StringVar()
        self.todo_status_var = StringVar()
        self.new_task_var = StringVar()

        for i, todo in enumerate(self.json_data['todo']):
            self.todo_task_var.set(todo['task'])
            self.todo_status_var.set(todo['status'])
            self.treeview.insert('', 'end', values=(self.todo_task_var.get(), self.todo_status_var.get()))

        #ttk.Label(self.treeview_frame, text=f"New Task:").grid(column=1, row=1, sticky=E)
        ttk.Entry(self.treeview_frame, textvariable=self.new_task_var).grid(column=1, row=2, sticky=E)
        #ttk.Button(self.treeview_frame, text=f"Add Task", command=self.add_task).grid(column=1, row=3, sticky=E)

        ttk.Button(self.button_frame, text=f"Re-Download json", command=self.download_todo_json).grid(column=0, row=3, sticky=W)
        ttk.Button(self.button_frame, text=f"Reload json", command=self.get_json_data).grid(column=1, row=3, sticky=W)
        ttk.Button(self.button_frame, text=f"Exit", command=self.exit).grid(column=2, row=3, sticky=W)
        ttk.Button(self.button_frame, text=f"Run LocalHost", command=self.run_localhost).grid(column=3, row=3, sticky=W)
        ttk.Button(self.button_frame, text=f"Exit LocalHost", command=self.exit_localhost).grid(column=4, row=3, sticky=W)
        ttk.Button(self.button_frame, text=f"Update Status", command=self.update_status_button_click).grid(column=5, row=3, sticky=W)
        ttk.Button(self.button_frame, text=f"Add Task", command=self.add_task).grid(column=6, row=3, sticky=W)
        ttk.Button(self.button_frame, text=f"Delete Task", command=self.delete_task_button_click).grid(column=5, row=4, sticky=W)
        ttk.Button(self.button_frame, text=f"Update Json", command=self.upload_json).grid(column=6, row=4, sticky=W)
        ttk.Button(self.button_frame, text=f"Delete api-key", command=self.del_api_key).grid(column=0, row=4, sticky=W)
        ttk.Button(self.button_frame, text=f"Delete FileID", command=self.del_fileid).grid(column=1, row=4, sticky=W)

        for child in self.mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        for child in self.button_frame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        for child in self.treeview_frame.winfo_children(): 
            child.grid_configure(padx=30, pady=5)

        for child in self.lastupdate.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

    def get_json_data(self): # Reloads the json file on the GUI
        super().get_json_data()

    def download_todo_json(self): # Re-Download the json file
        download_jsonbin()

    def exit_localhost(self):# Closes the localhost 
        print('LocalHost is closing..')
        self.p2.terminate() #Only with multiprocessing
        # self.p2.join() #Only with threading
        time.sleep(2)
        if self.p2.is_alive():
            print('LocalHost is still running')
        else:
            print('LocalHost is closed')

    def run_localhost(self): # Runs the localhost
        self.p2 = multiprocessing.Process(target=LocalHost.runlocalhost, args=("0.0.0.0", 5000)) #Only with multiprocessing
        print('LocalHost is executing..')
        time.sleep(2)
        self.p2.start()

    def exit(self): # Exits the program
        print("Exiting the editor...")
        time.sleep(2)
        self.root.destroy()

    def update_task_status(self, task_index, new_status):
        if task_index < len(self.json_data['todo']):
            self.json_data['todo'][task_index]['status'] = new_status
            self.save_jsonbin()
            print (f"Task status updated: {self.json_data['todo'][task_index]['task']} - {self.json_data['todo'][task_index]['status']}")
            self.get_json_data()
            print (f'Last update: {self.json_date['date']}')
        else:
            print("Invalid task index")

    def update_status_button_click(self):
        try:
            selected_item = self.treeview.selection()[0] 
            selected_item = self.treeview.index(selected_item)

            self.json_date['date'] = datetime.datetime.now().strftime('%Y-%m-%d')

            if self.json_data['todo'][selected_item]['status'] == 'Not completed':
                new_status = 'Completed'
            if self.json_data['todo'][selected_item]['status'] == 'Completed':
                new_status = 'Not completed'

            self.update_task_status(selected_item, new_status)

        except IndexError:
            print('No task selected')

    def save_jsonbin(self): # Save the json file
        save_backup_jsonbin(self.json_data)

    def add_task(self):
        print("Task Length: ",len(self.new_task_var.get()))
        if len(self.new_task_var.get()) > 0:
            print("New task added:", self.new_task_var.get())
            self.json_data['todo'].append({'task': self.new_task_var.get(), 'status': 'Not completed'})
            self.save_jsonbin()
            self.get_json_data()
            self.new_task_var.set('')
        else:
            print('No Task entered')

    def delete_task(self, task_index:int):
        if task_index < len(self.json_data['todo']):

            print (f"Task deleted: {self.json_data['todo'][task_index]['task']} - {self.json_data['todo'][task_index]['status']}")

            # Remove the task from the json data
            del self.json_data['todo'][task_index]

            # Save the updated json data to the file
            self.save_jsonbin()

            self.get_json_data()

        else:
            print("Invalid task index")

    def delete_task_button_click(self):
        try:
            selected_item = self.treeview.selection()[0]
            selected_item = self.treeview.index(selected_item)

            self.json_date['date'] = datetime.datetime.now().strftime('%Y-%m-%d')

            self.delete_task(selected_item)

        except IndexError:
            print('No task selected')
    
    def upload_json(self):
        upload_jsonbin(self.json_data)

    def del_api_key(self):
        with open(api_file_path + "JSONBINKEY", 'w') as f:
            f.write('')
            print('"JSONBINKEY" deleted')

    def del_fileid(self):
        with open(api_file_path + "FileID", 'w') as f:
            f.write('')
            print('"FileID" deleted')

    def run(self): # Runs the GUI
        self.root.mainloop()

class ApiKeyEditor(ToDoListGUI):
    def __init__(self, root):
        self.root = root
        self.user = self.get_user()
        self.root.title(f"{self.user}'s To-Do List Api-Key Editor")
        self.root.resizable(False, False)

        self.JSONBIN_API_KEY = StringVar()
        self.FileID = StringVar()

        self.current_JSONBIN_API_KEY = StringVar()
        self.current_FileID = StringVar()

        self.mainframe = ttk.Frame(self.root)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        for i in range(5):
            self.root.columnconfigure(i, weight=1)
            self.root.rowconfigure(i, weight=1)

        self.entry_frame = ttk.Frame(self.mainframe)
        self.entry_frame.grid(column=0, row=1, sticky=(N, W, E, S))

        self.current_api_keys()

        ttk.Label(self.entry_frame, text="Api-Key:").grid(column=0, row=0, sticky=W)
        ttk.Entry(self.entry_frame, textvariable=self.JSONBIN_API_KEY).grid(column=1, row=0, sticky=(W, E))

        # ttk.Label(self.entry_frame, text="Current JSONBIN Api-Key:").grid(column=0, row=2, sticky=W)
        # ttk.Label(self.entry_frame, textvariable=self.current_JSONBIN_API_KEY).grid(column=1, row=2, sticky=(W, E))

        ttk.Label(self.entry_frame, text="FileID:").grid(column=0, row=1, sticky=W)
        ttk.Entry(self.entry_frame, textvariable=self.FileID).grid(column=1, row=1, sticky=(W, E))

        # ttk.Label(self.entry_frame, text="Current FileID:").grid(column=0, row=3, sticky=W)
        # ttk.Label(self.entry_frame, textvariable=self.current_FileID).grid(column=1, row=3, sticky=(W, E))

        jsonbin_io_hyperlink = ttk.Label(self.entry_frame, text="Jsonbin.io", font=("Arial", 10, "bold", "underline"), foreground="blue")
        jsonbin_io_hyperlink.grid(column=0, row=6, sticky=W)
        jsonbin_io_hyperlink.bind("<Button-1>", lambda e: self.jsonbin_io())

        ttk.Button(self.entry_frame, text="Upload Template Json", command=self.upload_template).grid(column=0, row=2, columnspan=2, sticky=(W, E))
        ttk.Button(self.entry_frame, text="Save", command=self.save_api_keys).grid(column=0, row=3, columnspan=2, sticky=(W, E))
        ttk.Button(self.entry_frame, text="Save & Exit", command=self.save_and_exit).grid(column=0, row=4, columnspan=2, sticky=(W, E))
        ttk.Button(self.entry_frame, text="Exit", command=self.exit).grid(column=0, row=5, columnspan=2, sticky=(W, E))

        ttk.Label(self.mainframe, text=f"{self.user}'s To-Do List Api-Key Editor", font=("Arial", 16, "bold", "underline")).grid(column=0, row=0, sticky=W)

    def current_api_keys(self):
        with open(api_file_path + "JSONBINKEY", "r") as api:  
            self.JSONBIN_API_KEY.set(api.read().strip())
        with open(api_file_path + "FileID", "r") as id:  
            self.FileID.set(id.read().strip())

    def save_api_keys(self):
        with open(api_file_path + "JSONBINKEY", "w") as api:  
            print('Saving JSONBIN Api-Key...')
            api.write(self.JSONBIN_API_KEY.get())
        with open(api_file_path + "FileID", "w") as id:  
            print('Saving FileID...')
            id.write(self.FileID.get())

    def save_and_exit(self):
        self.save_api_keys()
        self.exit()

    def jsonbin_io(self):
        jsonbin_io_main()

    def bins(self):
        jsonbin_io_bins()

    def make_template(self):
        with open(api_file_path + "JSONBINKEY", "r") as api:
            api = api.read().strip()
            template = make_jsonbin({'date': datetime.datetime.now().strftime('%Y-%m-%d'), 'todo': [{'task': '', 'status': 'Not completed'}]},api)
        return template

    def upload_template(self):
        self.save_api_keys()
        template =self.make_template()
        if template.status_code == 200:
            self.bins()
        else:
            print(template.status_code, template.reason)
            print('Failed to upload file')

    def exit(self): # Exits the program
        self.root.destroy()
    
    def run(self): # Runs the GUI
        self.root.mainloop()

def mainWindow():
    root = Tk()
    root.geometry((f"{int(root.winfo_screenwidth()/2.8)}x{int(root.winfo_screenheight()/2.8)}"))
    gui = ToDoListGUI(root)
    gui.run()

def editorWindow():
    rootEditor = Tk()
    rootEditor.geometry((f"{int(rootEditor.winfo_screenwidth()/2.8)}x{int(rootEditor.winfo_screenheight()/2.6)}"))
    guiEditor = ToDoListEditor(rootEditor)
    guiEditor.run()

def ApiKeyWindow():
    rootEditor = Tk()
    rootEditor.geometry((f"{int(rootEditor.winfo_screenwidth()/4)}x{int(rootEditor.winfo_screenheight()/4)}"))
    guiEditor = ApiKeyEditor(rootEditor)
    guiEditor.run()

if __name__ == "__main__":
    pass
