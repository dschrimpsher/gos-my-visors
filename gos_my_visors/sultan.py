

class Sultan:
    def __init__(self, **config):
        self.name = config.get('name')
        self.visor_collection = config.get('visors')

    def __str__(self):
        temp = self.name + '\n'
        temp = '---------------------------------'
        temp = str(self.visor_collection)
        return temp

