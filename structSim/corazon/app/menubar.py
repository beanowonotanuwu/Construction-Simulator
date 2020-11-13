### IMPORTS                         ###
from tkinter import ttk     # ttk > tk; tk is not maintained in python 3
from tkinter import filedialog  # for opening files
from tkinter import (
    Menu
)
### IMPORTS                         ###
### MENU                            ###
class Menubar(Menu):
    def __init__(self, master, *args, **kwargs):
        ## Init                         ##
        super().__init__(master=master, *args, **kwargs)
        ## Init                         ##
        ## Menus                        ##
        construct_menu = Construct(self, tearoff=0)
        ## Menus                        ##
        ## Cascades                     ##
        self.add_cascade(
            label="Construct",
            menu=construct_menu
        )
        ## Cascades                     ##
### MENU                            ###
### CONSTRUCT MENU                  ###
class Construct(Menu):
    def __init__(self, master, *args, **kwargs):
        ## Init                         ##
        super().__init__(master=master, *args, **kwargs)
        ## Init                         ##
        ## Commands                     ##
        self.add_command(label="Select Construct...")
        self.add_command(label="Edit Construct...")
        self.add_separator()
        self.add_command(label="Close Construct")
        self.add_command(label="Close Application", command=master.quit)
        ## Commands                     ##
### CONSTRUCT MENU                  ###
