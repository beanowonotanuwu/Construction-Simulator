### IMPORTS                         ###
from corazon.app import App
from corazon.app.menubar import Menubar
### IMPORTS                         ###
### __MAIN__                        ###
if __name__ == "__main__":
    app = App()
    app.config(menu=Menubar(app))
    app.mainloop()
### __MAIN__                        ###