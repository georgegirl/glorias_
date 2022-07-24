
# # for x in range(10):
# #     print(x)

# # a = [3,4,5,6,7,8]

# # b = [x**2 for x in a] # list comprehension
# # print(b)

# # # or
# # b=[]
# # for i in a:
# #     b.append(i**2)


# # c = [x for x in a if x%2==0]
# # print (c)

# # d = [x if x%2==0 else 0 for x in a]
# # print(d)


# d = input("enter your data: ")
# for d in range(10):
#     if d %2==0:
#         print("true")
#     if d %2 !=0:
#         print("false")
#         break



# from math import sqrt

# def is_prime(n:int):

#     if n == 1:
#         return False

#     if n == 2:
#         return True

#     for factor in range(2, int(sqrt(n))+1):
#         if n % factor ==0:
#             return False

#     return True

# print(is_prime(12))





let_1= "eliminate"
let_2= "limit"

if sorted(let_1)  == sorted(let_2):
    print("false")
else:
    print("true, they're anagrams")


#OR

def anagrams(str1,str2):
    if sorted(str1)== sorted(str2):
        return True
    return False

print(anagrams("teach", "cheat"))