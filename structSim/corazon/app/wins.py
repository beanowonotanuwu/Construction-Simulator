### IMPORTS                             ###
from tkinter import Tk as tk_Tk
from tkinter import Frame as tk_Frame
from corazon.app.frames import main
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

        for F in (main.FRAMES):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(main.Main)
    ## Init                                 ##
    ## Funcs                                ##
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
    ## Funcs                                ##
### MAIN                                ###