### IMPORTS                         ###
from tkinter import Frame as tk_Frame
from tkinter.ttk import Button as ttk_Button
from tkinter.ttk import Style as ttk_Style
from corazon.util import setpath as u_setpath
from easyyaml import load as eyaml_load
### IMPORTS                         ###
### STYLES                          ###
    ## Loads                            ##
with u_setpath(r'Construction-Simulator\structSim\corazon\app\frames\styles', 2) as _:
    btn_dict = eyaml_load('buttons.yml').to_dict()

        # ignore                            #
    BTN_IGNORE = btn_dict['IGNORE']
        # ignore                            #
    ## Loads                            ##
    ## Settings                         ##
big_btn_set = {
    k:v for k, v in btn_dict['big'].items() if k not in BTN_IGNORE
}
    ## Settings                         ##
_style = ttk_Style()
_style.configure(btn_dict['big']['name'], **big_btn_set)
styles = {
    "btn": btn_dict['NAMES']
} # empty dict
### STYLES                          ###
### MAIN FRAME                      ###
class Main(tk_Frame):
    def __init__(self, parent, controller):
        ## Init                         ##
        tk_Frame.__init__(self, parent)
        self.control = controller
        ## Init                         ##
        ## Buttons                      ##
        load_construct_btn = ttk_Button(
            self,
            text="Load Construct",
            command=lambda *_: print(_),    # dummy cmd
            style=styles['btn']['big']
        )
            # display                       #
        load_construct_btn.grid(row=0, column=0)
            # display                       #
        ## Buttons                      ##
### MAIN FRAME                      ###
### FRAMES CONSTANT                 ###
FRAMES = (Main,)
### FRAMES CONSTANT                 ###