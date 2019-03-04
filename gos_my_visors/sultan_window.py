from gos_my_visors.sultan_frame import get_visor_header, get_visor_row
from tkinter import *

class SultanWindow:
    def __init__(self, sultan):
        self.root = Tk()
        self.root.title('Sultan')
        self.frame = Frame(self.root)
        self.frame.grid()
        self.sultan_label = Label(self.frame, font=("Brush Script MT", 24), text=sultan.name).grid(
            row=0, columnspan=5)
        self.sultan = sultan

        get_visor_header(self.frame, 1)

        index = 2
        for name, visor in sultan.visor_collection.visors.items():
            get_visor_row(visor, self.frame, index)
            index += 1
        self.root.mainloop()

