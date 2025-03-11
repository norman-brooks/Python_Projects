# Parent class

class Mammals:
    name = "Unknown"
    species = "Unknown"
    legs = None
    arms = None
    origin = "Unknown"
    carbon_based = True

    def information(self):
        msg = "\nName: {} \nSpecies: {}\nLegs: {}\nArms: {}\nOrigin: {}\nCarbon Based: {}".format(self.name, self.species, self.legs, self.arms, self.origin, self.carbon_based) 
        return msg

# Child classes below

class Human(Mammals):
    name = "Bob Dobbs"
    species = "Human"
    legs = 2
    arms = 2
    origin = "Earth"

    def trait(self):
        msg = "\nI slack, therfore I am"
        return msg
class Dog(Mammals):
    name = "Dolce"
    species = "Canine"
    legs = 4
    arms = 0
    origin = "Earth"

    def bark(self):
        msg = "\nI run to catch the rabbit"
        return msg
# We use the __init__ method on cat

class Cat(Mammals):
    def __init__(self, name, species, legs, fav_toy):
        self.name = name
        self.species = species
        self.legs = legs
        self.fav_toy = fav_toy

    def purpose(self):
        print("Hello, my name is", self.name, "the", self.species, "and my favorite toy is a", self.fav_toy,"!")
        
# The block above is for the object method. Below is where the info is

c1 = Cat("Mittens", "cat", 4, "ball of yarn")
c1.purpose()








if __name__ == "__main__":
    # Here is where we do the instantiantions
    human = Human()
    print(human.information())
    print(human.trait())

    dog = Dog()
    print(dog.information())
    print(dog.bark())
