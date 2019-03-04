from tkinter import *
from gos_my_visors.visor_frame import get_visor_details


class VisorWindow:
    def __init__(self, visor):
        self.root = Tk()
        self.root.title('Visor Details')
        self.frame = Frame(self.root)
        self.frame.grid()
        self.visor_label = Label(self.frame, font=("Brush Script MT", 24), text=visor.name).grid(
            row=0, columnspan=5)
        self.visor = visor

        get_visor_details(visor, self.frame, 1)
        self.root.mainloop()

