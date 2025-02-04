# class BankAccount():
#     def __init__(self,balance):
#         self.__balance=balance
#     def  deposit(self,amount):
#         self.__balance+=amount
#     def get_balance(self):
#         return  self.__balance


# account=BankAccount(1100)
# account.deposit(50)
# print(account.get_balance())
# # a=account.__balance
# # # print(a) #throw an error as .__balance is private

# class Computer():
#     def __init__(self,brand,model):
#         self.__brand=brand
#         self.__model=model
#     def get_info(self):
#         print(f"Model : {self.__model} Brand : {self.__brand}")

# comp1=Computer("HP","Infernus")
# comp1.get_info()
# print(comp1.__brand)
        

#<-----------------------Bank Account Project--------------------------------------->
class BankAccount():
    def __init__(self,account_number,initial_balance=0):
        self.__balance=initial_balance
        self.__account_number=account_number
    def deposit(self,deposit_amount):
        self.__balance=self.__balance + deposit_amount
        return self.__balance
    def withdrawl(self,withdrawl_amount):
        if(self.__balance>withdrawl_amount):
             self.__balance=self.__balance-withdrawl_amount
             return self.__balance
        else:
            return "Not sufficient Balance"
    def check(self):
        return self.__balance
    

account={}
from random import randint

while True:
    choice=int(input("What operation do you want to perform : \n1) Create Account\n2) Deposit\n3) Withdrawl\n4) Create Balance\n5) Exit\nChoose an option :"))
    match choice:
        case 1:
            acc_num=int("110077"+str(randint(300000,399999)))
            if(acc_num not in account):

                    print(f"New account is successfully created,your account number is {acc_num}")
                    ch=input("Do you want to deposit some initial amount (Y/N) : ")
                    if(ch in "Yy"):
                        in_amt=int(input("How much initial amount : ₹"))
                        user_account=BankAccount(acc_num,in_amt)
                    else:
                        user_account=BankAccount(acc_num)
                    account[acc_num]=user_account
        case 2:
            acc_num=int(input("Enter the account number :"))
            if(acc_num in account):
                   deposit_amt=int(input("How much amount do you want to  deposit : ₹"))
                   amt=account[acc_num].deposit(deposit_amt)
                   print(f"The current balance in your account is ₹{amt}")
            else:
                print(f"No account found with account number : {acc_num}")
        case 3:
            acc_num=int(input("Enter the account number :"))
            if(acc_num in account):
                   withdrawl_amt=int(input("How much amount do you want to  withdrawl : ₹"))
                   amt=account[acc_num].withdrawl(withdrawl_amt)
                   print(f"The current balance in your account is ₹{amt}")
            else:
                print(f"No account found with account number : {acc_num}")
          
        case 4:
            acc_num=int(input("Enter the account number :"))
            amt=account[acc_num].check()
            print(f"The current balance in your account is ₹{amt}")

        case 5:
            break
            
    print(account)



