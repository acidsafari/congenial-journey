# CREATING CLASSES
class PartyAnimal:
    x=0
    def party(self) :
        self.x = self.x + 1
        print("So far",self.x)

an = PartyAnimal() #this is when the object is constructed
an.party() #calling the party method
an.party()
an.party()
PartyAnimal.party(an) #another way to call the method within an object
'''
the class keyword defines a template indicating what data and code will be contained
in each object of type PartyAnimal.
'''

# A NEW CONSTRUCTOR
class PartyAnimal:
    x=0
    name = ''
    def __init__(self, nam): #self parameter that points to the object instance
        self.name = nam # additional parameters that are passed into the constructor
        print(self.name,'constructed')

    def party(self) :
        self.x = self.x + 1
        print(self.name,'party count',self.x)

s = PartyAnimal('Sally')
j = PartyAnimal('Jim')

s.party()
j.party()
s.party()
