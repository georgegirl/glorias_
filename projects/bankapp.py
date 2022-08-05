# # print("I CAN DO THIS WITH GOD, I KNOW I CAN")
# '''Write a program that allows customers to:
# 1. Create an account with the account number generated if they do not have an account. All generated account numbers should begin with 0
# 2. Log in to the program if they have an account
# 3. Deposit money
# 4. Withdraw money from the account if they have a sufficient amount.
# 5. Users should be able to transfer money to other users in the account
# 6. Users should be able to check their account balances.
# The program should keep running until the user decides to make it log out and/or quit.
# The account data should be stored in a dictionary that looks like that below and kept in a file for persistent storage'''



# import string
# import random

# accounts= {}
# Account_no= 0
# Customer_name= " "
# mobile_no= 0
# Bank_code='GG123'
# pin= 1234
# balance= 0


# # def in_it(self, name):
# #     self.name= name
# #     accounts[self.name] = 0

# def create_account(self):
#     username= input (" enter name: ")
#     print("current balance: ", balance)
#     number="0123456789"
#     whole="0"
#     string= whole + number
#     length= 10
#     account= "".join(random.sample(string, length))
#     account_num= whole + account
#     print("issued Account number: ", account_num)
#     print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#     login()
        

# def showacnt_detail(data):
#     print("Account no", account_num )
#     print("customer name: ", Customer_name)
#     print("bank code: ", Bank_code)
#     print("mobile number: ",mobile_no)
#     print("Password: ", pin)
     

# # def login(data):
# #     print(input("Account name: "))
# #     print(input("Password: "))
# #     showacnt_detail()
# def deposit (data, amount):
#     balance= balance + amount
#     print("Your Account has been credited with: $", balance)

# def withdraw(data ,amount):
#     balance= balance - amount
#     print("Current balance: $", balance)

# def transfer(data, receiver,  amount):
#     data.withdraw(amount)
#     receiver.deposit(amount)

# def checkbalance():
#     r = print("current balance:", balance)
#     return r


# def login(data:dict, account_no: int, balance:float):
    
#     """This function takes a dictionary, asks the user for the name and adds their name to the dictionary.
    
#     Args:
#         data(dict) : This is the dictionary that stores the user data
    
#     Returns:
#         name (str): This is the name of the user
#     """

    
#     name = input("Name: ").lower()

#     data[name] = balance
#     return name


# choice1= "y"
# while choice1:
#     print(" 1. create account \n 2. log in \n 3. withdr1awal \n 4. deposit \n 5. check balance")
#     choice= input("select any option")
#     if choice == 1:
#         print(create_account())
#     elif choice== 2:
#         login()
#     elif choice== 3:
#         amount=input("enter amount withdraw: ")
#         deposit(amount)
#     elif choice== 3:
#         amount=input("enter amount to deposite: ")
#         deposit(amount)
#     elif choice== 4:
#         checkbalance()
#     else:
#         print("please select any option")
#     break
# print("do you want to continue....Y/N")
# choice1= input()


data = {'0123445677' : {
        "first_name":"John",
        "last_name" : "Doe ",
        "login_pin" : "8424",
        "transaction_pin": "0934",
        "balance" : 0}
        }

def login():
    login = input('enter acct number.\n')
    if login in data.keys:
        login_pin = input('enter login pin.\n')
        if login_pin == data[login]['login_pin']:
            option = input('1. w\n 2d\n 3.t\n4.cab')
            options =[1,2,3,4]
            if option in options:
                if option == 1:
                    print('w')

                if option == 2:
                    print('d')
                
                if option == 3:
                    print('t')

                if option == 4:
                    print('cab')

            else:
                print('invalid input')

login()
        

# def deposit ():
#     amount=int(input("Amount to be deposited: "))
#     data['0123445677']['balance']+= amount
#     print("Your Account has been credited with: $", amount)

# deposit()
