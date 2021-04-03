class PartyAnimal:
    x = 0
    
    def __init__(self):
        print("It is a constructer")
    
    def party(self):
        self.x = self.x + 1
        print("X: ",self.x)
        
    def __del__(self):
        print("It is a destructer")

an = PartyAnimal()

an.party()
an.party()
an.party()

print(type(an))
print(dir(an))

an = 23
print("End of the class")

################################

ls = list()
print(type(ls)) # something about variable
print(dir(ls)) # command lists capabilities

################################

class CrazyAnimal:
    x = 1
    name = ""
    
    def __init__(self, z):
        self.name = z
        print("Name: ",self.name)
    
    def party(self):
        mul = 2
        if self.name == "Cat":
            mul = 3
        self.x = self.x * mul
        print(self.name," X: ", self.x)
    
    def __del__(self):
        self.x = 0
        print("End of the ",self.name," - ",self.x)
        
chicken = CrazyAnimal("Chicken")
chicken.party()
chicken.party()
chicken.party()

cat = CrazyAnimal("Cat")
cat.party()
cat.party()
cat.party()















