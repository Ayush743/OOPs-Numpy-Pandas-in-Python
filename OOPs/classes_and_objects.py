name="Ayush"
age=21        #These variables are the objects and instances  of classes str,int,bool etc
is_Anime_lover=True
# print(type(name),type(age),type(is_Anime_lover))

# first method to declare a object attribute
class Vechicle():
    def __init__(self):   #python executes the init function or constructor automatically
        print("I am created")

# car=Vechicle()
# truck=Vechicle()
# car.name="MercedesBenz"
# car.wheels=4
# print(car)

#Python tries to pass the first argument as object itself in the class methods so self is the mandatory argument that is to be given
import csv
class Item():
    pay_rate=0.8
    items_dict={}
    items_list=[]
    def __init__(self, id:int, name:str, price:int, qty :0):
        # run validations using assert statements
        assert price>=0 ,f"Price {price} must be greater than zero"
        assert qty>=0  
        #assign to self objects
        self.id=id
        self.name=name
        self.price=price
        self.qty=qty
        #actions to execute
        Item.items_dict[self.id]={
        "Name" : self.name,
        "Price" : self.price,
        "Qty" : self.qty}
        Item.items_list.append(self)
    def __repr__(self):
        #use repr to represent the instance of the classes
        return f"{self.id}||{self.name}"
    


    def calculate_price(self):
        return self.price*self.qty

    def apply_discount(self):
         self.price*=round(self.pay_rate*self.qty,2)
         return self.price
    
    #make of python decorators  to  create a class method
    @classmethod
    def instantiated_from_csv(cls):
        f=open("OOPs-Numpy-Pandas-in-Python/OOPs/items.csv","r")
        reader=csv.DictReader(f)
        items=list(reader)
        for item in items:
            Item(item["Id"],item["Item Name"],int(item["Price"]),int(item["Quantity"]))

    


      


        
# item_01=Item("A001","Pen",10,10)
# item_02=Item("A002","Football",100,10)
# item_03=Item("A003","laptop",100,10)
# item_04=Item("A004","pokemon cards",100,10)
# item_05=Item("A005","phone",100,10)
# items_dict=Item.items_dict
# # items_list=Item.items_list
Item.instantiated_from_csv()
print(Item.items_dict)

# total_price=item_01.calculate_price()
# discount_price=item_01.apply_discount()
# item_02.pay_rate=0.7
# # print(total_price)
# print(discount_price)
# print(item_02.apply_discount())
# print(Item.pay_rate)

# print(Item.__dict__)
# print()
# print(item_01.__dict__)

# items={}
# while True:
#     i_id=input("Enter the ID of the item : ")
#     i_name=input("Enter the name of the item : ")
#     i_price=int(input("Enter the price of the item :  ₹"))
#     i_qty=int(input("Enter the quantity of the item :"))
#     new_item=Item(i_id,i_name,i_price,i_qty)
#     items[new_item.id]={
#         "Name" : new_item.name,
#         "Price" : new_item.price,
#         "Qty" : new_item.qty
#     }
#     ch=input("Do you wish to add more items(Y/N) :")
#     if(ch in "Nn"):
#         break

    
# print(items)













#self keyword allows us to access the methods and variables of particular class and it is the first parameter for every method defined in class.




# class Person():
#     number_of_hands=2
#     def __init__(self,name,age):
#         print(f"hello my name is {name} and i am {age} old")
#         self.my_name=name
#     def walk(self):
#         print(f"{self.my_name} says I am going out for a walk")

# Person1=Person("Ayush",21)
# Person2=Person("Hinata",21)
# print(Person1.my_name)
# print(Person2.number_of_hands)


# class Car():
#     number_of_wheels=4
#     def __init__(self,maker,model):
#         # print(f"Car Name : {model} , Manufacturer : {maker} and has {Car.number_of_wheels} wheels")
#         self.maker=maker
#         self.model=model
        
# car1=Car("Volkwagen","virtus")
# car2=Car("Honda","Honda City")
# print(car1.model ,car1.number_of_wheels)
# class Citizen():
#     citizen_list=[]
#     def __init__(self,name:str,age:int,city : str,salary:int):
#         self.name=name
#         self.age=age
#         self.city=city
#         self.salary=salary

#         Citizen.citizen_list.append(self)
        
    
#     @classmethod
#     def instantiated_from_csv(cls):
#         f=open("OOPs-Numpy-Pandas-in-Python/OOPs/sample_data.csv","r")
#         reader=csv.DictReader(f)
#         data=list(reader)
#         for person in data:
#             Citizen(person["Name"],person["Age"],person["City"],person["Salary"])

#     def __repr__(self):
#         return f"( {self.name} || {self.city} || {self.age})"



# Citizen.instantiated_from_csv()
# print(Citizen.citizen_list)