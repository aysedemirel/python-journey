class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, nameCons):
        self.name = nameCons
        print("name: ", self.name)
    
    def party(self):
        self.x = self.x + 1
        print(self.name," - party count: ", self.x)


class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)
        

s = FootballFan("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()