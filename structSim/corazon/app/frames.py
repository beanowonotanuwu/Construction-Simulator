### IMPORTS                         ###
from tkinter import ttk     # ttk > tk; tk is not maintained in python 3
from tkinter import filedialog  # for opening files
from tkinter import (
    Frame
)
import corazon.util as util
from easyyaml import load
### IMPORTS                         ###
### LOADS                           ###
import os
print(os.getcwd(), 'asdasdad')
with util.setpath(r'Construction-Simulator\structSim\corazon\app', 2) as _:
    btn_styles = load('buttons.yml').to_dict()
    main_frame = load('main_frame.yml').to_dict()
    
    
    sel_construct = main_frame['sel_construct']

### LOADS                           ###
### FRAMES                          ###
class Main(Frame):
    def __init__(self, parent, controller):
        ## Init                         ##
        Frame.__init__(self, parent)
        ## Init                         ##
        ## Styles                       ##
        big = ttk.Style()
        big.configure("Big.TButton", **btn_styles['big'])
        ## Styles                       ##
        ## Buttons                      ##
        sel_construct_ = ttk.Button(
            self,
            text=sel_construct['text'],
            command=self.sel_construct_cmd,
            style=sel_construct['style']
        )
        edit_construct_ = ttk.Button(
            self,
            text=""
        )
            # commands                      #
            # commnads                      #
            # display                       #
        sel_construct_.grid(
            column=sel_construct['col'],
            row=sel_construct['row']
            )
            # display                       #
        ## Buttons                      ##
    ## Commands                         ##
    def sel_construct_cmd(self): self.selected_file = filedialog.askopenfilename(
        **sel_construct['cmd']
    )
    ## Commands                         ##
### FRAMES                          ###