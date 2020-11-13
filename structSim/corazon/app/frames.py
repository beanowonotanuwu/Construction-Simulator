### IMPORTS                         ###
from tkinter import ttk     # ttk > tk; tk is not maintained in python 3
from tkinter import filedialog  # for opening files
from tkinter import (
    Frame
)
import corazon.util as util
from easyyaml import load
from warnings import filterwarnings
### IMPORTS                         ###
### WARNINGS                        ###
filterwarnings("ignore", category=Warning)
### WARNINGS                        ###
### LOADS                           ###
with util.setpath(r'Construction-Simulator\structSim\corazon\app', 2) as _:
    btn_styles = load('buttons.yml').to_dict()
    main_frame = load('main_frame.yml').to_dict()
    load_construct = load('load_construct.yml').to_dict()
### LOADS                           ###
### FRAMES                          ###
class Main(Frame):
    def __init__(self, parent, controller):
        ## Init                         ##
        Frame.__init__(self, parent)
        self.sel_construct = main_frame['sel_construct']
        self.edit_construct = main_frame['edit_construct']
        self.settings = main_frame['settings']
        self.controller = controller
        ## Init                         ##
        ## Styles                       ##
        big = ttk.Style()
        big.configure("Big.TButton", **btn_styles['big'])
        ## Styles                       ##
        ## Buttons                      ##
        sel_construct_ = ttk.Button(
            self,
            text=self.sel_construct['text'],
            command=self.sel_construct_cmd,
            style=self.sel_construct['style']
        )
        edit_construct_ = ttk.Button(
            self,
            text=self.edit_construct['text'],
            command=self.edit_construct_cmd,
            style=self.edit_construct['style']
        )
        settings_ =  ttk.Button(
            self,
            text=self.settings['text'],
            style=self.settings['style']
        )
            # display                       #
        sel_construct_.grid(
            column=self.sel_construct['col'],
            row=self.sel_construct['row']
            )
        edit_construct_.grid(
            column=self.edit_construct['col'],
            row=self.edit_construct['row'],
            pady=self.edit_construct['pady']
        )
        settings_.grid(
            column=self.settings['col'],
            row=self.settings['row']
        )
            # display                       #
        ## Buttons                      ##
    ## Commands                         ##
    def sel_construct_cmd(self):
        selected_file = filedialog.askopenfilename(
            **self.sel_construct['cmd']
        )
        if selected_file: self.controller.show_frame(LoadConstruct)
    def edit_construct_cmd(self):
        selected_file = filedialog.askopenfilename(
            **self.edit_construct['cmd']
        )
        if selected_file: self.controller.show_frame(EditConstruct)
    ## Commands                         ##
class LoadConstruct(Frame):
    def __init__(self, parent, controller):
        ## Init                         ##
        Frame.__init__(self, parent)
        ## Init                         ##
        label = ttk.Label(self, text="LLJ")
        label.grid(row=0,column=0)
class EditConstruct(Frame):
    def __init__(self, parent, controller):
        ## Init                         ##
        Frame.__init__(self, parent)
        ## Init                         ##
        label = ttk.Label(self, text="LLJW")
        label.grid(row=0,column=0)
### FRAMES                          ###
FRAMES = (Main, LoadConstruct, EditConstruct)