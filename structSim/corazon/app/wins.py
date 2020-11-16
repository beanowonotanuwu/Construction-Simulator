### IMPORTS                             ###
from tkinter import Tk as tk_Tk
from tkinter import Frame as tk_Frame
### IMPORTS                             ###
### MAIN                                ###
class Main(tk_Tk):
    ## Init                                 ##
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # container                             #
        container = tk_Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # container                             #
        self.frames = {}

        for F in (0,):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(0)
    ## Init                                 ##
    ## Funcs                                ##
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
    ## Funcs                                ##
### MAIN                                ###