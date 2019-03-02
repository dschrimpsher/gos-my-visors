

class Visors:
    def __init__(self, visors):
        self.visors = {}
        for visor in visors:
            self.visors[visor.name] = visor

    def __str__(self):
        for name, visor in self.visors.items():
            print(visor)