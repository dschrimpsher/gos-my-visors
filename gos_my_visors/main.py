import csv
from gos_my_visors.visor import Visor
from gos_my_visors.visor_collection import Visors
from tkinter import *

visor_collection = None
frame = None
root = None

def load(visors):
    pass


def init():
    global visor_collection
    visors = []
    filename = 'visors.csv'
    with open(filename, 'r', newline='') as csvfile:
        counter = 0
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if counter < 3:
                pass
                counter += 1
            elif row[1] is '':
                pass
            elif row[9] is '':
                pass
            else:
                base = {}
                base['name'] = row[1]
                base['military stars'] = []
                base['military levels'] = []
                base['research stars'] = []
                base['research levels'] = []
                base['politics stars'] = []
                base['politics levels'] = []
                base['prestige stars'] = []
                base['prestige levels'] = []
                for index in range(9, 16):
                    if row[index] is not '-' and row[index] is not '':
                        try:
                            base['military stars'].append(int(row[index]))
                        except ValueError:
                            print('Error', row[index])
                        base['military levels'].append(1)
                for index in range(16, 22):
                    if row[index] is not '-' and row[index] is not '':
                        try:
                            base['research stars'].append(int(row[index]))
                        except ValueError:
                            print('Error', row[index])
                        base['research levels'].append(1)
                for index in range(22, 27):
                    if row[index] is not '-' and row[index] is not '':
                        try:
                            base['politics stars'].append(int(row[index]))
                        except ValueError:
                            print('Error', row[index])
                        base['politics levels'].append(1)
                for index in range(27, 32):
                    if row[index] is not '-' and row[index] is not '':
                        try:
                            base['prestige stars'].append(int(row[index]))
                        except ValueError:
                            print('Error', row[index])
                        base['prestige levels'].append(1)
                visor = Visor(**base)
                visors.append(visor)
    visor_collection = Visors(visors)
    print("Good")


def main():
    init()
    global frame
    global root
    root = Tk()
    frame = Frame(root)
    frame.grid()

    w = Label(frame, text="GoS Visor Manager")
    w.grid(row=0, columnspan=2)

    tl = Label(frame, text="Sultan Name")
    t = Entry(frame)
    tl.grid(row=1, column=0)
    t.grid(row=1, column=1)

    b = Button(frame, text="New Game")
    b.grid(row=2, column=0)

    b2 = Button(frame, text="Load Game")
    b2.grid(row=2, column=1)

    v = []
    table = Frame(frame)
    table.grid(row=3, columnspan=2)
    index = 0
    for name, visor in visor_collection.visors.items():
        cb =Checkbutton(table).grid(row=index, column=0)
        temp = Label(table, text=name).grid(row=index, column=1)
        v.append(temp)
        index += 1
    # if visor_collection is not None:
    #     index = 0
    #     for name, visor in visor_collection.visors.items():
    #         temp = Label(table, text=name).grid(row=index)
    #         index += 1

    root.mainloop()


if __name__ == "__main__":
    # execute only if run as a script
    main()