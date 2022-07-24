# '''Write a program that allows customers to:
# 1. Create an account with the account number generated if they do not have an account. All generated account numbers should begin with 0
# 2. Log in to the program if they have an account
# 3. Deposit money
# 4. Withdraw money from the account if they have a sufficient amount.
# 5. Users should be able to transfer money to other users in the account
# 6. Users should be able to check their account balances.
# The program should keep running until the user decides to make it log out and/or quit.
# The account data should be stored in a dictionary that looks like that below and kept in a file for persistent storage'''
# import random





# # balance= 0
# # data = {
# #     '0123445677' : {
# #         "first_name":"John",
# #         "last_name" : "Doe ",
# #         "login_pin" : "8424",
# #         "transaction_pin": "0934",
# #         "balance" : 0
# #     }
# # }
# # # class accounts():
# # def login(data:dict, account_no: int, balance:float):
# #     """This function takes a dictionary, asks the user for the name and adds their name to the dictionary.

# # Args:
# #     data(dict) : This is the dictionary that stores the user data

# # Returns:
# #     name (str): This is the name of the user
# # """
# #     name = input("Name: ").lower()
# #     data[name] = balance
# #     return name

# def account_no_gen():
#     number="0123456789"
#     whole="0"
#     string= whole + number
#     length= 10
#     account= "".join(random.sample(string, length))
#     account_num= whole + account
#     rt = print(" Your issued Account number: ", account_num)
#     return rt

# def input_login():
#     user_name1= input("first name:  ").capitalize()
#     user_name2= input("second name: ").capitalize()
#     name=print("hi {} {}, welcome to the George's bank".format(user_name1, user_name2))
#     return name

# def deposit ():
#     amount=int(input("Amount to be deposited: "))
#     data['0123445677']['balance']+= amount
#     print("Your Account has been credited with: $", amount)

# # # deposit()

# # print(data)


# def withdraw():
#     amount= float(input("Enter Amount to be withdrawn: "))
#     balance= balance - amount
#     if amount <= balance:
#         print("you withdrew ", amount)
#     elif amount > balance:
#         print("insufficient balance")
#     else:
#         print('incorrect input')

# def checkbalance(data):
#         return "current balance:", balance

# def transfer():
   
# def generate_pin(data):
#     number="0123456789"
#     whole="0"
#     string= whole + number
#     length= 4
#     account= "".join(random.sample(string, length))
#     pin = whole + account
#     token =print("issued transaction pin: ", pin)
#     return token
    
# def login_pin(data):
#     login=input("choose your login pin")
#     length= 4
#     return login


# data={}
# print("welcome to the George's bank")
# print("The passion of banking")
# status= input("do you have an account? \nYES/NO: ").upper()
# g ="NO"
# r= "YES"
# if status== g:
#     account= print(account_no_gen())
#     print("dear customer, do well to remember ")
#     login_pin(data)
#     print("your pin is {}, do keep to yourself".format(login_pin(data)))
#     if account not in data:
#         user_name1= input("first name:  ").capitalize()
#         user_name2= input("second name: ").capitalize()
#         trans= generate_pin(data)
#         balance=checkbalance(data)
#         data= {}
#         name=print("hi {} {}, welcome to the George's bank".format(user_name1, user_name2))
#         print("Account created {}".format(user_name1))
#         data.update({account_no_gen:{"first_name":user_name1,"second_name":user_name2, "login pin": login_pin,"Transaction pin": trans, "account balance": balance }})
#         print(data)
# if status == r:
#     log= input("input login ")
#     if log == login_pin:
#         print("welcome {} customer".format(user_name1))
#         print("what service would you like")
#         print("1. withdrawal \n 2. deposit \n 3. check balancen\n 4. transfer")
#         choice=input("select any option")
#         if choice== 1:
#             en = input("login pin")
#             if en== login_pin:
#                 withdraw(data)
#             else:
#                 print("Sorry {} Incorrect pin".format(user_name1))
#         if choice==2:
#             en= input("login pin")
#             if en== login_pin:
#                 deposit (data)
#             else:
#                 print("Sorry {} Incorrect pin".format(user_name1))
#         if choice==3:
#             en= input('login pin')
#             if en== login_pin:
#                 checkbalance(data)
#             else:
#                 print("Sorry {} Incorrect pin".format(user_name1))
#         if choice == 4:
#             en == input("login pin")
#             if en == login_pin:
                

# continue1 = input("WOULD YOU LIKE TO PLAY AGAIN {}. ENTER YES/NO: ".format(user_name1)).lower()
# g= "yes"
# h= "no"

    
# with open("databasecode.txt", "r") as file:
#     data = eval(file.read())
#     print(type(data))


'''Write a program that allows customers to:
1. Create an account with the account number generated if they do not have an account. All generated account numbers should begin with 0
2. Log in to the program if they have an account
3. Deposit money
4. Withdraw money from the account if they have a sufficient amount.
5. Users should be able to transfer money to other users in the account
6. Users should be able to check their account balances.
The program should keep running until the user decides to make it log out and/or quit.
The account data should be stored in a dictionary that looks like that below and kept in a file for persistent storage'''
import random


print("Welcome to The George's Bank ")
print("The passion of banking")

with open("databasecodes.txt", "r") as in_put:
    data = eval(in_put.read())

data= {}

def account_no_gen():
    number="0123456789"
    whole="0"
    string= whole + number
    length= 10
    account= "".join(random.sample(string, length))
    account_num= whole + account
    rt = print(" Your issued Account number: ", account_num)
    return rt

def generate_pin():
    number="0123456789"
    whole="0"
    string= whole + number
    length= 4
    account= "".join(random.sample(string, length))
    pin = whole + account
    token = pin
    return token

transaction_pin= generate_pin()




# def continue1(): 
#     continue_OH = int(input("Do you wish to:\n.1. back menu \n2. log out"))
#     print(continue_OH)

# continue1()

program = False
while not program:
    start= input("do you have an account? \nYES/NO: ").lower()
    if start == "yes":
        account = input("give your account number")
        if account in data.keys():
            print ("welcome", data[account]["first_name", data[account]["second_name"]])
            login_pin=input("enter your login pin: ")
            print("dear customer, do well to remember ")
            if login_pin == data[account]["login_pin"]: 
                print("what service would you like")
                options= ("1. withdrawal \n 2. deposit \n 3. check balancen\n 4. transfer")
                choice= input("select any option")

                if choice in options:
                    pin = data[account]["transaction_pin"]
                    if choice == 1:
                        log= input("enter transaction pin: ")
                        if log == pin:
                            withdraw_1= int(input("enter amount to be withdrawn: "))
                            balan_ = data[account]["balance"]
                            if withdraw_1 > balan_:
                                print("insufficient balance")
                                print("You have {} remaining".format(balan_))
                                continue_OH = int(input("Do you wish to:\n.1. back menu \n2. log out"))
                                
                            else:
                                data[account]["balance"]-= withdraw_1
                                print("You have been debited {}".format(withdraw_1))
                                print("Your New Balance is ${}".format(balan_))
                                # continue1():

                        else:
                            print("incorrect pin")
                            # continue1()

                    elif choice == 2:
                        log= input("enter transaction pin: ")
                        if log == pin:
                            depo_= int(input(" enter amount: "))
                            data[account]["balance"]+= depo_
                            print("Current balance is ${}".format(data[account]["balance"]))
                            # continue1()/
                        else:
                            print("incorrect pin")
                            # continue1()

                    elif choice == 3:
                        log= input("enter transaction pin: ")
                        if log == pin:
                            print("$", data[account]["balance"])
                            # continue1()
                        else:
                            print("incorrect pin")
                            # continue1()


                    elif choice == 4:
                        user= input("enter user account number: ")
                        if user in data:
                            amount= int(input("enter amount: $ "))
                            log= input("enter transaction pin: ")
                            if log== pin:
                                data[user]["balance"]+= amount
                                data[account]["balance"]-=amount
                                print(f'$ {amount} has been transferred to {user}', data[user]["first_name"], data[user]["last_name"])
                                # continue1()
                            else:
                                print("incorrect pin")
                                # continue1()
                        else:
                            print("user not found")
                            break
                else:
                    print("invalid input")
                    break

                with open("databasecodes.txt", "w") as in_put:
                    in_put.write(str(data))


            else: 
                print("incorrect pin") 
                # continue1() 


        else:
            print("user not found")
            # continue1()
    
    
    elif start == "no":
        intro = generate_pin()
        if intro not in data:
            print("Your Account number is {}, keep for future use".format(intro))
            data.update({f'{intro}': {"first_name": " ",
                                    "second_name": " ",
                                    "login_pin": " ",
                                    "transaction_pin": " ",
                                    "balance": 30000
                                      }})
            info = input(" state your first_name: ")
            data[intro]["first_name"]= info
            info2= input("state your second_name: ")
            data[intro]['second_name']= info2
            info3= print("transaction pin", generate_pin())
            data[intro]["transaction_pin"]= info3
            info4= input("set login pin: ")
            data[intro]["login_pin"]=info4


            print("dear {} {}, your account has been succesfully created".format(info, info2))
            print("welcome to The George's Bank")
            print("Thank you for banking with us")
            with open("databasecodes.txt", "w") as in_put:
                in_put.write(str(data))

    else:
        print("nvalid input")

    # def continue1(): 
    #     continue_OH = int(input("Do you wish to:\n.1. back menu \n2. log out"))
    #     if continue_OH == 1:
    #         continue

    #     elif continue_OH == 2:
    #         print("Thank You For Banking With The George's ")
    #         print("Till Next Time")
    #         break

    #     else:
    #         print("Bye For Now")
    #         break


    

    
        
                            

                        

                        
                



        




