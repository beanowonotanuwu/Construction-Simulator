### IMPORTS                         ###
from corazon.app.wins import Main
from corazon.app.menubar import Menubar
### IMPORTS                         ###
### __MAIN__                        ###
if __name__ == "__main__":
    main = Main()
    main.title("Main - Construct Sim")
    # main.config(menu=Menubar(main))
    main.mainloop()
### __MAIN__                        ###