# word= ("lacuna, peacemaker, woman, gloria, indomie")
# peacemaker
# woman
# gloria
# indomie
# lacuna
# from ast import Not
# from multiprocessing import RLock
# import random
# word_list = []
# word_file = open("fifthclass.py/exercise.txt")
# for word in word_file:
#     word_list.append(word.strip())
# answer= random.choice(word_list)
# word= answer
# tries_count= 0
# tries = 4
# display= "-"*len(answer)
# n= 0
# game_over= False
# print(" WELCOME GAMER")
# print("GAME STARTS NOW")
# print("choose from below")
# print("abcdefghijklmnopqrstuvwxyz")
# print(answer)


# while not game_over: #and tries != word
#     print("YOU HAVE" + " " + str (tries) + " "  +"TRIES" +  " " + "REMAINING" )
#     print(display)
#     guess= input("ENTER WORD ")
    
#     if guess in word:
#         while word.find(guess, n) != -1:
#            n = word.find(guess, n)
#            display = display[:n] + guess + display[n + 1:]
#            n += 1
#         print("correct")
#     else:
#         print("wrong guess.")
#         tries -= 1  
#     if tries == 0:
#         print("SORRY ATTEMPT USED UP")
#         game_over= True

#     if word== display:
#        print("YOU WIN! THE WORD WAS  " + word)
#        game_over= True  
    


    # if tries_count < tries:
    #     print(display)
    #     game_over = True


#     if guess in word:
#         i= word.find(guess)
#         display= display[ :i] + guess + display[i + 1:]
# print("YOU WIN")
# from multiprocessing import parent_process


# # k = [78,90,40,60,20,20,60,20,50,90,90,40,20,30,20]
# # print(max(set(k), key = k.count))
# # print(set(k))
# # print(k.count())
# # ''' an alternative of this would be to give two parameters which provides the set of k 
# # and each set being counted, then finding the maximum occurance of k.

# '''
import string 
import random


g4= string.digits
g1= 0

print(g4)

try:
    generated_an= int("enter your password lenght: ")
    g=[]
    g.extend(list(g4))
    g.extend(g1)


    random.shuffle(g)
    print(f"generated account no : {''.join(g[:generated_an])}")

except Exception as e:
    print("invalid account no.")
