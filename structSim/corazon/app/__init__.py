### IMPORTS                         ###
from tkinter import Tk      ## for inheritance
from tkinter import ttk     ## ttk > tk; tk is not maintained in python 3
from corazon.app import frames
### IMPORTS                         ###
### APP CLASS                       ###
class App(Tk):
    def __init__(self, *args, **kwargs):
        ## Init                         ##
        Tk.__init__(self, *args, **kwargs)
        ## Init                         ##
        ## Displaying Frames            ##
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in frames.FRAMES:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(frames.Main)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

        ## Displaying Frames            #
### APP CLASS                       ###