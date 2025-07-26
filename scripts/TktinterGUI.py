from tkinter import *
from tkinter import ttk

import os
import multiprocessing
import time



if __name__ == '__main__':
    from jsonbin import load_jsonbin, download_jsonbin
    import localhostHTML as LocalHost
else:
    from scripts.jsonbin import load_jsonbin, download_jsonbin
    import scripts.localhostHTML as LocalHost

# def download_todo_json():
#     download_jsonbin()

# def mainWindow():
#     root = Tk()
#     root.geometry((f"{int(root.winfo_screenwidth()/3)}x{int(root.winfo_screenheight()/3)}"))
#     todo_date_var = StringVar()
#     todo_task_var = StringVar()
#     todo_status_var = StringVar()
#     root.title("Nahida's To-Do List")
#     root.resizable(False, False)

#     mainframe = ttk.Frame(root, padding="0 0 120 0")
#     mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
#     for i in range(5):
#         root.columnconfigure(i, weight=1)
#         root.rowconfigure(i, weight=1)

#     ttk.Label(mainframe, text="Nahida's To-Do List", font=("Arial", 16, "bold", "underline")).grid(column=0, row=0, sticky=E)

#     todo_date_var.set(json_date['metadata']['createdAt'].replace('T', '/').replace('Z', '').split('/')[0])

#     ttk.Label(mainframe, text="Last update: ", font=("Arial", 12, "bold")).grid(column=0, row=1, sticky=E)
#     ttk.Label(mainframe, textvariable=todo_date_var, font=("Arial", 12)).grid(column=1, row=1, sticky=W)

#     todo_row = 2
#     todo_column = 0

#     ToDoframe = ttk.Frame(mainframe)
#     ToDoframe.grid(column=todo_column+1, row=todo_row, sticky=NSEW)
#     for i in range(5):
#         ToDoframe.columnconfigure(i, weight=1)
#         ToDoframe.rowconfigure(i, weight=1)

#     scrollbar = ttk.Scrollbar(ToDoframe, orient=VERTICAL, takefocus=True)
#     scrollbar.grid(column=todo_column+2, row=todo_row, sticky=E)

#     treeview = ttk.Treeview(ToDoframe, yscrollcommand=scrollbar.set)
#     treeview.grid(column=todo_column+1, row=todo_row, sticky=N+S+W)

#     scrollbar.config(command=treeview.yview)

#     treeview['columns'] = ('todo', 'status')

#     treeview.column("#0", width=0, stretch=NO)
#     treeview.column("todo", anchor=W, width=200)
#     treeview.column("status", anchor=W, width=100)

#     treeview.heading("#0", text="", anchor=W)
#     treeview.heading("todo", text="To-Do", anchor=W)
#     treeview.heading("status", text="Status", anchor=W)

#     for i, todo in enumerate(json_data['record']['todo']):
#         todo_task_var.set(todo['task'])
#         todo_status_var.set(todo['status'])
#         treeview.insert('', 'end', values=(todo_task_var.get(), todo_status_var.get()))

#     button_row = 3
#     button_column = 1

#     ButtonFrame = ttk.Frame(mainframe)
#     ButtonFrame.grid(column=button_column, row=button_row, sticky=N+S+W+E)
#     for i in range(5):
#         ButtonFrame.columnconfigure(i, weight=1)
#         ButtonFrame.rowconfigure(i, weight=1)

#     ttk.Button(ButtonFrame, text=f"Re-Download json", command=download_todo_json).grid(column=button_column+1, row=button_row, sticky=E)
#     ttk.Button(ButtonFrame, text=f"Update json", command=Reload).grid(column=button_column+2, row=button_row, sticky=W)

#     for child in mainframe.winfo_children(): 
#         child.grid_configure(padx=5, pady=5)

#     for child in ButtonFrame.winfo_children(): 
#         child.grid_configure(padx=5, pady=5)

#     for child in ToDoframe.winfo_children(): 
#         child.grid_configure(padx=5, pady=5)

#     root.mainloop()

class ToDoListGUI:
    def __init__(self, root):
        self.root = root
        self.user = self.get_user()
        self.root.title(f"{self.user}'s To-Do List")
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
            print("Error: No se pudo cargar el icono. Asegúrate de que el archivo 'icon.ico' exista y esté en la ruta correcta.")
        except FileNotFoundError:
            print("Error: El archivo 'icon.ico' no se encontró.")
        except Exception as e:
            print(f"Error inesperado: {e}")

        self.json_date = {'metadata': {'createdAt': '0000-00-00T00:00:00.000Z'}}
        self.json_data = {'record': {'todo': [{'task': 'Reload Json', 'status': 'To be Done'}]}}
        

        self.mainframe = ttk.Frame(self.root, padding="0 0 120 0")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        for i in range(5):
            self.root.columnconfigure(i, weight=1)
            self.root.rowconfigure(i, weight=1)

        ttk.Label(self.mainframe, text=f"{self.user}'s To-Do List", font=("Arial", 16, "bold", "underline")).grid(column=0, row=0, sticky=E)

        self.todo_date_var = StringVar()
        self.todo_date_var.set(self.json_date['metadata']['createdAt'].replace('T', '/').replace('Z', '').split('/')[0])

        ttk.Label(self.mainframe, text="Last update: ", font=("Arial", 12, "bold")).grid(column=0, row=1, sticky=E)
        ttk.Label(self.mainframe, textvariable=self.todo_date_var, font=("Arial", 12)).grid(column=1, row=1, sticky=W)

        self.treeview_frame = ttk.Frame(self.mainframe)
        self.treeview_frame.grid(column=1, row=2, sticky=N+S+W+E)
        for i in range(5):
            self.treeview_frame.columnconfigure(i, weight=1)
            self.treeview_frame.rowconfigure(i, weight=1)

        self.button_frame = ttk.Frame(self.mainframe)
        self.button_frame.grid(column=1, row=3, sticky=N+S+W+E)
        for i in range(5):
            self.button_frame.columnconfigure(i, weight=1)
            self.button_frame.rowconfigure(i, weight=1)

        self.treeview = ttk.Treeview(self.treeview_frame, columns=('todo', 'status'))
        self.treeview.grid(column=1, row=2, sticky=N+S+W)

        self.treeview.column("#0", width=0, stretch=NO)
        self.treeview.column("todo", anchor=W, width=200)
        self.treeview.column("status", anchor=W, width=100)

        self.treeview.heading("#0", text="", anchor=W)
        self.treeview.heading("todo", text="To-Do", anchor=W)
        self.treeview.heading("status", text="Status", anchor=W)

        self.todo_task_var = StringVar()
        self.todo_status_var = StringVar()

        for i, todo in enumerate(self.json_data['record']['todo']):
            self.todo_task_var.set(todo['task'])
            self.todo_status_var.set(todo['status'])
            self.treeview.insert('', 'end', values=(self.todo_task_var.get(), self.todo_status_var.get()))

        ttk.Button(self.button_frame, text=f"Re-Download json", command=self.download_todo_json).grid(column=0, row=3, sticky=E)
        ttk.Button(self.button_frame, text=f"Reload json", command=self.get_json_data).grid(column=1, row=3, sticky=W)
        ttk.Button(self.button_frame, text=f"Exit", command=self.exit).grid(column=2, row=3, sticky=E)
        ttk.Button(self.button_frame, text=f"Run LocalHost", command=self.run_localhost).grid(column=3, row=3, sticky=W)
        ttk.Button(self.button_frame, text=f"Exit LocalHost", command=self.exit_localhost).grid(column=4, row=3, sticky=W)

        for child in self.mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        for child in self.button_frame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        for child in self.treeview_frame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

    def get_json_data(self): # Reloads the json file on the GUI
        self.json_data = load_jsonbin()

        self.json_date = self.json_data
        self.json_data = self.json_data

        self.todo_date_var.set(self.json_date['metadata']['createdAt'].replace('T', '/').replace('Z', '').split('/')[0])
        self.treeview.delete(*self.treeview.get_children())
        for i, todo in enumerate(self.json_data['record']['todo']):
            self.todo_task_var.set(todo['task'])
            self.todo_status_var.set(todo['status'])
            self.treeview.insert('', 'end', values=(self.todo_task_var.get(), self.todo_status_var.get()))

        print("Json reloaded")
        
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
        #self.p2 = multiprocessing.Process(target=LocalHost.runlocalhost, args=())
        print('LocalHost is executing..')
        time.sleep(2)
        self.p2.start()

    def exit(self): # Exits the program
        print("Exiting the program...")
        time.sleep(2)
        if self.p2.is_alive() == True:
            self.p2.terminate() #Only with multiprocessing
            # self.p2.join() #Only with threading
        else :
            print('LocalHost is closed')
        self.root.destroy()


    def run(self): # Runs the GUI
        self.root.mainloop()

def mainWindow():
    root = Tk()
    root.geometry((f"{int(root.winfo_screenwidth()/2.5)}x{int(root.winfo_screenheight()/3)}"))
    gui = ToDoListGUI(root)
    gui.run()

if __name__ == "__main__":
    mainWindow()
