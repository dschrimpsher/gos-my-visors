from tkinter import *


def get_visor_details(visor, parent, starting_row):
    Label(parent, text='----------------------------------------------').grid(row=starting_row+1, columnspan=4)
    Label(parent, text='Attributes: ' + str(visor.get_attributes())).grid(row=starting_row+2, columnspan=4)
    Label(parent, text='Military Attributes').grid(row=starting_row+3, column=0)
    Label(parent, text=str(visor.military_attributes())).grid(row=starting_row+3, column=1)

    Label(parent, text='Research Attributes').grid(row=starting_row+3, column=2)
    Label(parent, text=str(visor.research_attributes())).grid(row=starting_row+3, column=3)

    Label(parent, text='Political Attributes').grid(row=starting_row+4, column=0)
    Label(parent, text=str(visor.political_attributes())).grid(row=starting_row+4, column=1)

    Label(parent, text='Prestige Attributes' + str(visor.prestige_attributes())).grid(row=starting_row+4, column=2)
    Label(parent, text=str(visor.prestige_attributes())).grid(row=starting_row+4, column=3)

    Label(parent, text='------------------------------------').grid(row=starting_row+5, columnspan=4)
    Label(parent, text='Talent: ' + str(visor.get_talent())).grid(row=starting_row+6, columnspan=4)

    row = starting_row+7
    column = 0
    for index in range(len(visor.military_stars)):
        Label(parent, width=15, text='Military Stars').grid(row=row, column=column)
        Label(parent, text=get_stars(visor.military_stars[index])).grid(row=row, column=column+1)
        Label(parent, width=15, text='Military Level').grid(row=row+1, column=column)
        Spinbox(parent, width=4, from_=visor.military_level[index], to=350).grid(row=row+1, column=column+1)
        Label(parent, width=15, text='Military Talent').grid(
            row=row+2, column=column)
        Label(parent, width=15, text=str(visor.military_stars[index]*visor.military_level[index])).grid(row=row+2,
                                                                                              column=column+1)
        column += 2
        if column is 4:
            Label(parent, text='---------------').grid(row=row + 3, columnspan=4)
            column = 0
            row += 4

    for index in range(len(visor.research_stars)):
        Label(parent, width=15, text='Research Stars').grid(row=row, column=column)
        Label(parent, text=get_stars(visor.research_stars[index])).grid(row=row, column=column + 1)
        Label(parent, width=15, text='Research Level').grid(row=row + 1, column=column)
        Spinbox(parent, width=4, from_=visor.research_level[index], to=350).grid(row=row + 1, column=column + 1)
        Label(parent, width=15, text='Research Talent').grid(
            row=row + 2, column=column)
        Label(parent, width=15, text=str(visor.research_stars[index] * visor.research_level[index])).grid(row=row + 2,
                                                                                                          column=column + 1)
        column += 2
        if column is 4:
            Label(parent, text='---------------').grid(row=row + 3, columnspan=4)
            column = 0
            row += 4

    for index in range(len(visor.political_stars)):
        Label(parent, width=15, text='Political Stars').grid(row=row, column=column)
        Label(parent, text=get_stars(visor.political_stars[index])).grid(row=row, column=column + 1)
        Label(parent, width=15, text='Political Level').grid(row=row + 1, column=column)
        Spinbox(parent, width=4, from_=visor.political_level[index], to=350).grid(row=row + 1, column=column + 1)
        Label(parent, width=15, text='Political Talent').grid(
            row=row + 2, column=column)
        Label(parent, width=15, text=str(visor.political_stars[index] * visor.political_level[index])).grid(row=row + 2,
                                                                                                          column=column + 1)
        column += 2
        if column is 4:
            Label(parent, text='---------------').grid(row=row + 3, columnspan=4)
            column = 0
            row += 4

    for index in range(len(visor.prestige_stars)):
        Label(parent, width=15, text='Prestige Stars').grid(row=row, column=column)
        Label(parent, text=get_stars(visor.prestige_stars[index])).grid(row=row, column=column + 1)
        Label(parent, width=15, text='Prestige Level').grid(row=row + 1, column=column)
        Spinbox(parent, width=4, from_=visor.prestige_level[index], to=350).grid(row=row + 1, column=column + 1)
        Label(parent, width=15, text='Prestige Talent').grid(
            row=row + 2, column=column)
        Label(parent, width=15, text=str(visor.prestige_stars[index] * visor.prestige_level[index])).grid(row=row + 2,
                                                                                                          column=column + 1)
        column += 2
        if column is 4:
            Label(parent, text='---------------').grid(row=row + 3, columnspan=4)
            column = 0
            row += 4

def get_stars(num):
    temp = ''
    for i in range(num):
        temp += '*'
    return temp