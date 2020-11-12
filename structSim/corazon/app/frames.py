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
        sel_construct = ttk.Button(
            self,
            text="Select Construction",
            command=self.sel_construct_cmd,
            style="Big.TButton"
        )
            # commands                      #
            # commnads                      #
            # display                       #
        sel_construct.grid(row=0,column=0)
            # display                       #
        ## Buttons                      ##
    ## Commands                         ##
    def sel_construct_cmd(self): self.selected_file = filedialog.askopenfilename(
        **main_frame['sel_construct']
    )
    ## Commands                         ##
### FRAMES                          ###