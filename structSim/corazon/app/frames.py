### IMPORTS                         ###
from tkinter import ttk     ## ttk > tk; tk is not maintained in python 3
from tkinter import (
    Frame
)
import corazon.util as util
from easyyaml import load
### IMPORTS                         ###
### LOADS                           ###
import os
print(os.getcwd(), 'asdasdad')
with util.setpath(r'Construction-Simulator\structSim\corazon\app', 2) as _: main_frame = load(
    'main_frame.yml'
).to_dict()
### LOADS                           ###
### FRAMES                          ###
class Main(Frame):
    def __init__(self, parent, controller):
        ## Init                         ##
        Frame.__init__(self, parent)
        ## Init                         ##
        ## Buttons                      ##
        sel_model = ttk.Button(
            self,
            **main_frame['sel_model']
        )
        sel_model.grid(row=0,column=0)
        ## Buttons                      ##
### FRAMES                          ###