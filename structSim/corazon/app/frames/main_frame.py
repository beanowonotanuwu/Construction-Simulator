### IMPORTS                         ###
from tkinter import Frame as tk_Frame
from tkinter.ttk import Button as ttk_Button
from tkinter.ttk import Style as ttk_Style
from corazon.util import setpath as u_setpath
from easyyaml import load as eyaml_load
### IMPORTS                         ###
### STYLES                          ###
with u_setpath(r'Construction-Simulator\structSim\corazon\app\frames\styles', 2) as _:
    btn_dict = eyaml_load('buttons.yml').to_dict()

# import pdb; pdb.set_trace()
_style = ttk_Style()
_style.configure(btn_dict['big']['name'])
styles = {
    "btn": (btn_dict['NAMES'])
} # empty dict
print(styles)
### STYLES                          ###
### MAIN FRAME                      ###
class Main(tk_Frame):
    def __init__(self, parent, controller):
        ## Init                         ##
        super().__init__(parent)
        self.control = controller
        ## Init                         ##
        ## Buttons                      ##
        ## Buttons                      ##
### MAIN FRAME                      ###
### FRAMES CONSTANT                 ###
FRAMES = (Main,)
### FRAMES CONSTANT                 ###