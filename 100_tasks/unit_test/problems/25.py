class Animal:
    name="Animal"

    def __init__(self,name=None):
        self.name=name

kangaroo=Animal("Kangaroo")
print("{} name is {}".format(Animal.name,kangaroo.name))

wombat=Animal("Wombat")
print("{} name is {}".format(Animal.name,wombat.name))
