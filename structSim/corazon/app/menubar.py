### IMPORTS                         ###
from tkinter import ttk     # ttk > tk; tk is not maintained in python 3
from tkinter import filedialog  # for opening files
from tkinter import (
    Menu, Label
)
from tkinter import font
### IMPORTS                         ###
### MENU                            ###
class Menubar(Menu):
    def __init__(self, master, *args, **kwargs):
        ## Init                         ##
        super().__init__(master=master, *args, **kwargs)
        self.master = master
        ## Init                         ##
        ## Menus                        ##
        construct_menu      = Construct(self, tearoff=0)
        view_menu           = ViewMenu(self, tearoff=0)
        simulate_menu       = Simulate(self, tearoff=0)
        ## Menus                        ##
        ## Cascades                     ##
        self.add_cascade(
            label="Construct",
            menu=construct_menu
        )
        self.add_cascade(
            label="View",
            menu=view_menu
        )
        self.add_cascade(
            label="Simulate",
            menu=simulate_menu
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
### VIEW MENU                       ###
class ViewMenu(Menu):
    def __init__(self, master, *args, **kwargs):
        ## Init                         ##
        super().__init__(master=master, *args, **kwargs)
        ## Init                         ##            
        ## Commands                     ##
        self.add_command(label="Fullscreen")
        ## Commands                     ##
### VIEW MENU                       ###
### SIMULATE MENU                   ###
class Simulate(Menu):
    def __init__(self, master, *args, **kwargs):
        ## Init                         ##
        super().__init__(master=master, *args, **kwargs)
        ## Init                         ##
        ## Commands                     ##
        self.add_command(label="Start with Statistics")
        self.add_command(label="Start without Statistics")
        self.add_command(label="Restart with Statistics")
        self.add_command(label="Restart without Statistics")
        self.add_command(label="Pause...")
        self.add_separator()
        self.add_command(label="Stop Simulation")
        ## Commands                     ##
### SIMULATE MENU                   ###