from tkinter import *
from gos_my_visors.visor_window import VisorWindow
from functools import partial


def get_visor_row(visor, parent, starting_row):
    action_with_arg = partial(VisorWindow, visor)
    Button(parent, text='view', command=action_with_arg).grid(row=starting_row, column=0)
    Label(parent, text=visor.name).grid(row=starting_row, column=1)
    Label(parent, text=visor.level).grid(row=starting_row, column=2)
    Label(parent, text=visor.military_talent()).grid(row=starting_row, column=3)
    Label(parent, text=visor.military_power()).grid(row=starting_row, column=4)


def get_visor_header(parent, starting_row):
    Label(parent, text='Edit').grid(row=starting_row, column=0)
    Label(parent, text='Visor').grid(row=starting_row, column=1)
    Label(parent, text='Level').grid(row=starting_row, column=2)
    Label(parent, text='Military Talent').grid(row=starting_row, column=3)
    Label(parent, text='Military Power').grid(row=starting_row, column=4)
