class Vehicle():
    def start_engine(self):
        print("Engine started")
    def drive(self):
        print("Lets drive")
class Car(Vehicle):
    pass
class Truck(Vehicle):
    def __init__(self):
        print("I am a truck")
    def start_engine(self): #overriding it means when the method defined in the superclass is modified by one of its subclass,in the given example the Truck subclass overrides the Vehicle superclass start_engine method.
        print("Truck Engine Roars for life !")

car1=Car()
car1.start_engine()

truck1=Truck()
truck1.start_engine()


class Animal:
    all=[]
    def __init__(self,name,species):
        self.name=name
        self.species=species
        Animal.all.append(self)

    def make_sound(self):
        print("I make sound")
    def desc(self):
        print(f"My name is {self.name},i am a {self.species}")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name} || {self.species})"
    
        
class Dog(Animal):
    
    def __init__(self, name, species,no_of_legs):
        super().__init__(name, species) # we have access to all the methods and variables created in the parent class
        self.num_legs=no_of_legs
        

    def make_sound(self):
        print("I bark")
    def desc(self):
        print(f"My name is {self.name},i am a {self.species} and i have {self.num_legs} legs")

dog1=Dog("Tommy","Dog",4)
cat1=Animal("Kitty","cat")
dog1.desc()
dog1.make_sound()
cat1.desc()
print(dog1.all)