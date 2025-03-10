class Vehicle:
        def __init__(self, year, make, model):
                self.year = year
                self.make = make
                self.model = model
    # Above is our Parent Class with an argument

        
    # Below are children classes of "Vehicle"
class Motorcycle(Vehicle):
        def __init__(self, year, make, model):
            super(). __init__(fuel)
            self.fuel = fuel


class Cycle(Vehicle):
        def __init__(self, year, make, model):
            super(). __init__(pedals)
            self.pedals = pedals

    # We use the Vehicle to create and object and THEN execute the printname method

def printveh(self):
    print(self.year, self.make, self.model, self.fuel)
    x = Vehicle(1971, "Harley", "Softtail", "Carbureted")
 
    x.printveh
