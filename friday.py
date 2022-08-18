import random

data = {}
with open("trans.txt","r") as file:
    data = eval(file.read())
with open("class.txt", "r") as file:
    data = eval(file.read())

def signup(details:dict, trans:dict):

    first_name= input("state first name buyer: ")
    second_name= input("state second name buyer: ")
    login_pin = input("state your login pin")
    trans_pin= input("state your transaction pin")


    code = "0"
    for i in range(9):
        login_in+= str(random.choice(range(6)))


        details[login_in] = {"first_name":first_name,
                    "second_name" : second_name,
                    "login_pin" : login_pin,
                    "transaction_pin": trans_pin,
                    "balance" : 0}

        trans[login_in] = []


    print(f"welcome {first_name} {second_name}, your account has been created. your account number is {code}. you can login to your account using your login pin: {login_pin}")
    return details, trans

def login(data: dict):
    print("WELCOME TO THE GEORG'S BANK\ninput your details")
    acc_num= input("Account number: ")
    login_pin= input("login pin: ")
    user_detail = data.get(acc_num)

    if user_detail and user_detail["login_pin"]== login_pin:
        return user_detail, acc_num

    else:
        return False

def deposit(user_detail: dict):
    
    amount = float(input("give amount to deposit: "))
    user_detail["balance"] += amount
    print(f"dear {user_detail['first_name']}, your account has been credited with {amount}")
    return user_detail, amount

def withdraw(user_detail:dict):
    trans_pin = input("Enter your pin: ")

    if trans_pin == user_detail["transaction_pin"]:
        amount= float(input("state amount to be transferred: "))

        if user_detail["balance"] > amount:
            user_detail["balance"] -= amount
            print(F"\nyou have successfully withdrawn #{amount}")
            return user_detail, amount
        else:
            print("insufficient funds to withdraw")

    else:
        print("incorrect pin")
        return

def transfer(user_detail:dict, data:dict):
    beneficiary= input("Enter beneficiary account: ")
    amount= float(input("how much to transfer: "))

    beneficiary_detail= data.get(beneficiary)
    if beneficiary_detail:
        if user_detail["balance"] > amount:
            user_detail["balance"] -= amount
            beneficiary_detail["balance"] += amount 
            print("transfer of #", {}, "was successfully transferred to", {beneficiary['first_name']}.format(amount))
            return user_detail, data, amount,  beneficiary

        else:
            amount = None
            print("insufficient funds to transfer")
            return user_detail, data, amount, beneficiary
    else:
        amount= None
        print("Account Not Recognized")
        return user_detail, data, amount, beneficiary

def update_transaction(trans_data:dict, acc_num:str, trans_type:str, action:str, amount:float):
    trans_detail = {
        "amount": amount,
        "action": action,
        "trans_type": trans_type,
    }
    trans_data[acc_num].append(trans_detail)
    return trans_data
 
print("WELCOME TO THE BANK")

while True:
    print("select any option\n====1.login\n====2.signup\n====3.logout")
    choice= input(">>>>")
    if choice =="2":
        data, trans_data = signup(data, trans_data)
    elif choice =="1":
        user_detail, acc_num = login(data)


        if user_detail:
            print("Welcome",user_detail["first_name"])
            while True:
                print("""Enter the corresponding number for the action you wish to perform.
                1.Check Balance
                2. Deposit
                3. Withdraw
                4. Transfer
                5. Recent Transactions
                6. Logout
                """)
                action = input("<>")
                if action == "1":
                    print(f"\nYour current balance is #{user_detail['balance']}")
                elif action == "2":
                    user_detail, amount = deposit(user_detail)
                    trans_data = update_transaction(trans_data, acc_num, "credit", "deposit", amount)
                elif action =="3":
                    user_detail, amount = withdraw(user_detail)
                    trans_data = update_transaction(trans_data, acc_num, "debit",
                    "withdraw", amount)
                elif action == "4":
                    user_detail, data, amount,beneficiary = transfer(user_detail, data)

                    if amount is not None:
                        trans_data = update_transaction(trans_data, acc_num, "debit","transfer", amount )
                        trans_data = update_transaction(trans_data, beneficiary, "credit", "transfer", amount)
                elif action == "5":
                    login_pin = trans_data.get(acc_num)
                    login_pin.reverse()
                    if len(login_pin) >= 5:
                        for i in range(5):
                            transcation = login_pin[i]
                            print("==================")
                            
                            print(f"action: {transcation['action']}")
                            print(f"Amount: # {transcation['amount']}")
                            print(f"transaction_type: {transcation['trans_type']}")
                        print("==================")
                    else:
                            for i in range(len(login_pin)):
                                transaction = login_pin[i]
                                print("================")
                                print(f"Amount: #{transaction['amount']}")
                                print(f"action: {transaction['action']}")
                                print(f"transaction type: {transaction['trans-type']}")
                            print("=================")
                elif action == "6":
                    print(f"Bye for now {user_detail['first_name']} ")
                    break
                else:
                    print("invalid input")
    elif choice =="2":
        data, trans_data = signup(data, trans_data)
    elif choice == "3":
        print("\nBye!")
        break
    else:
        print("\nInvalid input")

with open("trans.txt", "w") as file:
    file.write(str(data))
with open("class.txt", "w") as file:
    file.write(str(data))













    
     