
import string
import random
# CREATING PASSWORD USING SYMBOLS ALPHABETS AND DIGITS
# s1= string.ascii_lowercase
# s2= string.ascii_uppercase
# s3= string.digits
# s4= string.punctuation
# s5= string.__name__


# try:
#     plen = int(input("Enter your password length: "))
#     s =[]
#     s.extend(list(s1))
#     s.extend(list(s2))
#     s.extend(list(s3))
#     s.extend(list(s4))
#     s.extend(list(s5))

#     random.shuffle(s)
#     print(f"Your password : {''.join(s[:plen])}")

# except Exception as e:
#     print("its not a valid integer")




# #CREATING PASSWORD USING A GIVEN NAME'_'
# import random
# import string
# password_name= (list("george_gloria_rachel"))
# # print(password_name)

# try:
#     plen = int(input("Enter your password length: "))
#     password_name[0]
#     password_name[4]
#     password_name[3]
#     password_name[7]
#     password_name[9]
#     password_name[11]
#     password_name[18]
#     password_name[15]
#     password_name[13]
#     password_name[8]
#     password_name[6]
#     password_name[19]
#     password_name[16]
#     password_name[17]
#     password_name[12]
#     password_name[14]
#     password_name[15]
#     password_name[1]
#     password_name[2]
#     password_name[5]
#     password_name[10]

#     random.shuffle(password_name)
#     print(f" Your password: {''.join(password_name[:plen])}")
   
# except Exception as e:# this accept all exception that may occur in the code
#     print("its not a valid integer")

g4= (list(string.digits))
random.shuffle(g4)
# print(g4)
g1= [0]
# generated_an= (int(input("enter your password lenght: ")))
# g=[]
# g.extend(list(g4))
# g.extend(list(g1))

n= g4 + g1
# random.choice(n)
# list.reverse(n)
# print(n)
# print(" ".join(n))
# #RANGE
# # my_list = [6,8,0,2,4,10]
# print(my_list[3:5])  #SPLIT IN RANGE

# n= random.shuffle(g)
# print(f"generated account no : {''.join(g[:generated_an])}")

number="0123456789"
whole="0"
string= whole + number
length= 9
account= "".join(random.sample(string, length))
print(whole + account)


num="123456789"
whole="0"
lenght=10
random.shuffle(list(num))
print(whole+ num)

# g4= (list(string.digits))
# g1= 0,0,0
# generated_an= (int(input("enter your password lenght: ")))
# g=[]
# g.extend(g4)
# g.extend(list(g1))




# random.choice(g)
# print(f"generated account no : {''.join(g[:generated_an])}")
