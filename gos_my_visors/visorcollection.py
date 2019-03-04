

class VisorCollection:
    def __init__(self, visors):
        self.visors = {}
        for visor in visors:
            self.visors[visor.name] = visor

    def __str__(self):
        temp = ''
        for name, visor in self.visors.items():
            temp += str(visor)
        return temp

    def get(self, name):
        return self.visors[name]