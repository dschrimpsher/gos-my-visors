
class Visor:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.military_stars = kwargs.get('military stars')
        self.research_stars = kwargs.get('research stars')
        self.politics_stars = kwargs.get('politics stars')
        self.prestige_stars = kwargs.get('prestige stars')

        self.military_level = kwargs.get('military levels')
        self.research_level = kwargs.get('research levels')
        self.politics_level = kwargs.get('politics levels')
        self.prestige_level = kwargs.get('prestige levels')

        self.level = 1

    def __str__(self):
        temp = self.name + ':\n'
        mt = 0
        for index in range(len(self.military_stars)):
            mt += self.military_stars[index] * self.military_level[index]
        temp += 'military talent ' + str(mt)  + '\n'
        rt = 0
        for index in range(len(self.research_stars)):
            rt += self.research_stars[index] * self.research_level[index]
        temp += 'research talent ' + str(rt)  + '\n'
        pt = 0
        for index in range(len(self.politics_stars)):
            pt += self.politics_stars[index] * self.politics_level[index]
        temp += 'politics talent ' + str(pt)  + '\n'
        prt = 0
        for index in range(len(self.prestige_stars)):
            prt += self.prestige_level[index] * self.prestige_stars[index]
        temp += 'prestige talent ' + str(prt)  + '\n'
        return temp
