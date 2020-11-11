### IMPORTS                         ###
from tkinter import Tk      ## for inheritance
from tkinter import ttk     ## ttk > tk; tk is not maintained in python 3
from app import frames
### IMPORTS                         ###
### APP CLASS                       ###
class App(Tk):
    def __init__(self, *args, **kwargs):
        ## Init                         ##
        Tk.__init__(self, *args, **kwargs)
        ## Init                         ##
### APP CLASS                       ###