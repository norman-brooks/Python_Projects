class Assign:
    def __init__(self):
        self._var1 = 55 # Protected attribute
        self.__str1 = "Two Fives" # Private attribute

    def showVar(self):
        print(self._var1)
        print(self.__str1)

class Subassign(Assign): # Added a second function to see how children interact with encapsulation
    def __init__(self):
        self.__var2 = 23 # Private attribute
    def showVar2(self):
        return self._var2


obj = Assign() # Create an instance
obj.showVar() # Show the encapsulated variables
obj2 = Subassign() # create an instance of the child
# print(obj2.__var2) This will throw an error code since we can't directly reference var 2
print(obj._var1) # print this to show we can access a protected variable, but not a private one
        



