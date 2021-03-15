from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk

sroot = Tk()
sroot.minsize(height=200, width=300)
sroot.title(" ")
sroot.configure()
# Frame(sroot, height=516, width=5, bg='black').place(x=520, y=0)
lbl1 = Label(sroot, text="Welcome to The URI Food Pantry App!\n This app it intended to help organize your food, "
                         "and to know when it will go bad.", font='OldStandardTT 30 ', fg='black')

lbl1.config(anchor=CENTER)
lbl1.pack(padx=100, pady=100)
# lbl1.configure(background='')
# This is the button to kill the program and go right to the app
Button(sroot, text="Proceed to App", bg='red', command=sroot.destroy).pack(side=BOTTOM, fill=X)


def mainroot():
    root = Tk()
    root.geometry('1080x500')
    root.minsize(width=1080, height=550)
    root.maxsize(width=1080, height=550)
    root.configure(bg='Light Blue')


# This will then call our app and remove the splash screen after a certain amount of seconds,
def call_mainroot():
    sroot.destroy()


# Splash Screen will be on the screen for 3 seconds, then the app will open
sroot.after(10000, call_mainroot)  # TimeOfSplashScreen
mainloop()  # This is here so the two screens don't show up at the same time


# Below is the main functionality of our app
class Application(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.initialize_user_interface()

    def initialize_user_interface(self):
        # Configure the root object for the Application
        self.root.title("URI Food Pantry App")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.config(background="Light blue")

        # Define the different GUI widgets
        self.name_label = tk.Label(self.root, text="Food Name:")
        self.name_entry = tk.Entry(self.root)
        self.name_label.grid(row=0, column=0, sticky=tk.W)
        self.name_entry.grid(row=0, column=1)

        self.Quantity_label = tk.Label(self.root, text="Quantity:")
        self.Quantity_entry = tk.Entry(self.root)
        self.Quantity_label.grid(row=1, column=0, sticky=tk.W)
        self.Quantity_entry.grid(row=1, column=1)

        self.Bought_label = tk.Label(self.root, text="Date Bought:")
        self.Bought_entry = tk.Entry(self.root)
        self.Bought_label.grid(row=2, column=0, sticky=tk.W)
        self.Bought_entry.grid(row=2, column=1)

        self.Expiration_label = tk.Label(self.root, text="Expiration Date:")
        self.Expiration_entry = tk.Entry(self.root)
        self.Expiration_label.grid(row=3, column=0, sticky=tk.W)
        self.Expiration_entry.grid(row=3, column=1)

        self.submit_button = tk.Button(self.root, text="Insert", command=self.insert_data)
        self.submit_button.grid(row=3, column=2, sticky=tk.W)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.grid(row=0, column=3)

        # Set the treeview
        self.tree = ttk.Treeview(self.root, columns=('Name', 'Quantity', 'Date Bought', 'Expiration Date'))

        # Set the heading (Attribute Names)
        self.tree.heading('#1', text='Food Name')
        self.tree.heading('#2', text='Quantity')
        self.tree.heading('#3', text='Date Bought')
        self.tree.heading('#4', text='Expiration Date')

        # Specify attributes of the columns (this makes it able to stretch)
        # self.tree.column('#0', stretch=tk.YES)
        self.tree.column('#0', stretch=tk.YES)
        self.tree.column('#1', stretch=tk.YES)

        self.tree.grid(row=4, columnspan=4, sticky='nsew')
        self.treeview = self.tree

        self.id = 0

        self.iid = 0

    def insert_data(self):
        self.treeview.insert('', 'end',
                             values=(self.name_entry.get(), self.Quantity_entry.get(), self.Bought_entry.get(),
                                     self.Expiration_entry.get()))


app = Application(tk.Tk())
app.root.mainloop()
