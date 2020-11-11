### IMPORTS                         ###
from tkinter import ttk     ## ttk > tk; tk is not maintained in python 3
from tkinter import (
    Frame
)
### IMPORTS                         ###
### FRAMES                          ###
class Main(Frame):
    def __init__(self, parent, controller):
        ## Init                         ##
        Frame.__init__(self, parent)
        ## Init                         ##
        ## Buttons                      ##
        sel_model = ttk.Button(
            self,
            text='Select Model'
        )
        ## Buttons                      ##
### FRAMES                          ###