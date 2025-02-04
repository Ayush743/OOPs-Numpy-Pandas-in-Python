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