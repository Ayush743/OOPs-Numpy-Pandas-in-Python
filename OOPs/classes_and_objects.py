
#self keyword allows us to access the methods and variables of particular class and it is the first parameter for every method defined in class.
class Person():
    number_of_hands=2
    def __init__(self,name,age):
        print(f"hello my name is {name} and i am {age} old")
        self.my_name=name
    def walk(self):
        print(f"{self.my_name} says I am going out for a walk")

Person1=Person("Ayush",21)
Person2=Person("Hinata",21)
print(Person1.my_name)
print(Person2.number_of_hands)


class Car():
    number_of_wheels=4
    def __init__(self,maker,model):
        # print(f"Car Name : {model} , Manufacturer : {maker} and has {Car.number_of_wheels} wheels")
        self.maker=maker
        self.model=model
        
car1=Car("Volkwagen","virtus")
car2=Car("Honda","Honda City")
print(car1.model ,car1.number_of_wheels)
