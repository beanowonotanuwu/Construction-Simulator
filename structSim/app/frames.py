### IMPORTS                         ###
from tkinter import ttk     ## ttk > tk; tk is not maintained in python 3
from tkinter import (
    Frame
)
import load
import structSim.util as util
### IMPORTS                         ###
### FRAMES                          ###
class Main(Frame):
    def __init__(self, parent, controller):
        ## Init                         ##
        Frame.__init__(self, parent)
        ## Init                         ##
        ## Loads                        ##
        main_frame = util.load.LOADS['main_frame']
        ## Loads                        ##
        ## Buttons                      ##
        sel_model = ttk.Button(
            self,
            **main_frame['sel_model']
        )
        ## Buttons                      ##
### FRAMES                          ###