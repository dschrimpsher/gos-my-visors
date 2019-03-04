
class Visor:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.military_stars = kwargs.get('military stars')
        self.research_stars = kwargs.get('research stars')
        self.political_stars = kwargs.get('politics stars')
        self.prestige_stars = kwargs.get('prestige stars')

        self.military_level = kwargs.get('military levels')
        self.research_level = kwargs.get('research levels')
        self.political_level = kwargs.get('politics levels')
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
        for index in range(len(self.political_stars)):
            pt += self.political_stars[index] * self.political_level[index]
        temp += 'politics talent ' + str(pt)  + '\n'
        prt = 0
        for index in range(len(self.prestige_stars)):
            prt += self.prestige_level[index] * self.prestige_stars[index]
        temp += 'prestige talent ' + str(prt)  + '\n'
        return temp

    def military_talent(self):
        mt = 0
        for index in range(len(self.military_stars)):
            mt += self.military_stars[index] * self.military_level[index]
        return mt

    def research_talent(self):
        mt = 0
        for index in range(len(self.research_stars)):
            mt += self.research_stars[index] * self.research_level[index]
        return mt

    def political_talent(self):
        mt = 0
        for index in range(len(self.political_stars)):
            mt += self.political_stars[index] * self.political_level[index]
        return mt

    def prestige_talent(self):
        mt = 0
        for index in range(len(self.prestige_stars)):
            mt += self.prestige_stars[index] * self.prestige_level[index]
        return mt

    def military_attributes(self):
        """
        (talent/5) [(level-1)(level+2)/2 + 50]
        :return:
        """
        return (self.military_talent()/5.0) * ((self.level-1)*(self.level+2) / 2.0 + 50.0)

    def research_attributes(self):
        return (self.research_talent()/5.0) * ((self.level-1)*(self.level+2) / 2.0 + 50.0)

    def political_attributes(self):
        return (self.political_talent()/5.0) * ((self.level-1)*(self.level+2) / 2.0 + 50.0)

    def prestige_attributes(self):
        return (self.prestige_talent()/5.0) * ((self.level-1)*(self.level+2) / 2.0 + 50.0)

    def military_power(self):
        mp = self.level * self.military_talent() * 5000
        mp += self.military_attributes()
        return mp

    def get_attributes(self):
        at = self.military_attributes() + self.research_attributes() + self.political_attributes() + \
             self.prestige_attributes()
        return at

    def get_talent(self):
        at = self.military_talent() + self.research_talent() + self.political_talent() + \
             self.prestige_talent()
        return at
