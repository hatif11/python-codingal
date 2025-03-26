# class Person:

#     def __init__(self ,name , age):
#         self.name =name
#         self.age =age
#         print(f"hello guys my name is {self.name} And my age is about {self.age} years")
    
#     def welcome(self):
#         print(f'hello my name is {self.name} welcome to the class')

#     def __del__(self):
#         print (f"nice to meet you {self.name} your class ended and your data ids deleted")

# details = Person("starc",56)
# details.welcome()
# del details
# details.welcome()
#///////////////////////////////////////////////
class BankAccount:
    def __init__(self ,name, account_num,balance=0):
        self.name= name
        self.account_num= account_num
        self.balance = balance
        print(f"hello my name {self.name} i wanna buy car my aoccunt balance is {self.balance} and my account number is {self.account_num}")

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f'you have deposit your money and you current balance is {self.balance}')
        else:
            print('you failed in deposit you money')

    def withdraw(self,amount):
        if amount>0:
         self.balance-=amount
         print(f"you have successfully withdraw your payment and you balance is {self.balance}")
        else :
            print("invalde amount try again")

Account1=BankAccount("hatif",30993654636,500)
# Account2=BankAccount('Akash',99737543578,1000)
# Account3=BankAccount('varun',11111653410,1500)

Account1.deposit(500)
Account1.withdraw(200)