# from operator import not_
# import random
# user= input("WELCOME TO MY GAME")
# print(input("name: "))
# print("name")
# # print("CHOOSE A NUMBER TO PLAY")
# # game_play= list(range(9,90))
# # random.shuffle(game_play)

# # print(game_play)
# # users_play= int(input(">>>"))

# # com_choice= random.choice(game_play)
# # # print(users_play, com_choice)

# # # if users_play in game_play:
# # #     if users_play < com_choice:
# # #         print("too bad")
# # #         print("try again")
# # #     elif  users_play == com_choice:
# # #         print("CONGRATULATION")
# # #         print("YOU WIN")
# # #     else:
# # #         if users_play > com_choice:
# # #             print("have faith :)")
# # #             print("dont give up")


from pickle import FALSE
import random
print("WELCOME GAMER TO A WORLD OF PONZI SCHEMMES, DO WELL TO PLAY ")
print("DO WELL TO PLAY TO THE FULLIEST")
def greet(name):
   print(input(" STATE NAME" + (name)))
QUES_TION= (input("PLACE A BET"))
print("YOU HAVE THREE TRIES DO WELL TO USE THEM WISELY :) :) ")
print("START GAME")

game_exercise=list(range(1, 10))
random.shuffle(game_exercise)
print(game_exercise)

user_choice= int(input("state your number"))

comlong= random.choice(game_exercise)
print(user_choice, comlong)

if user_choice in game_exercise:
    if user_choice < comlong:
        print("LOST THE GAME :(")
        print("$5 LOST") 
    elif user_choice > comlong:
        print("TOO LOW")
        print("OH WELL")
        print("$5 LOST")
        print("TRY AGAIN ")
        print("START AGAIN")
    else:
        if user_choice == comlong:
            print("CONGRATULATION'S")
            print("NEXT STAGE")
            print("PLACE YOUR BET")
        else:
            if user_choice == (0):
                print("EXIT GAME")






# # # word= ("lacuna, peacemaker, woman, gloria, indomie")
# # # peacemaker
# # # woman
# # # gloria
# # # indomie
# # # lacuna
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
    


#     # if tries_count < tries:
#     #     print(display)
#     #     game_over = True


# #     if guess in word:
# #         i= word.find(guess)
# #         display= display[ :i] + guess + display[i + 1:]
# # print("YOU WIN")
# # from multiprocessing import parent_process




# import random
# print("WELCOME GAMER")
# print("instruction: choose between this variables ")
# print("rock, papers, scissors")
# list["g", "h", "l"]
# # a= random.choice(list)
# # game_exer = a
# com_choice= random.choice("ghl")
# tries= 2
# tries_con= 0
# g= "rock"
# h= "scissors"
# l= "papers"
# user_choice= input("state your choice: ").lower()
# print(com_choice)


# if user_choice in "ghi":
#     if user_choice==g and com_choice== h:
#         print("you win")
# elif com_choice== h and user_choice==l:
#         print("YOU LOST")
#         print("TRY AGAIN")
# if com_choice==g and user_choice==l:
#             print(" YOU LOST")
#             print("TRY AGAIN")
#             tries -=1
# if com_choice == h and user_choice== h:
#             print("YOU LOSE")
#             print("TRY AGAIN LATER")
# if user_choice== com_choice:
#             print("you draw")
#             print("OH MONALIZA")
# else:
#     if com_choice== l and user_choice==g:
#         print("you win")
#     if com_choice==g and user_choice==g:
#                 print ("DRAW")
#                 game_over= True
# if tries == 0:
#     print("attempt elapsed")
#     print("game_over")

# print("game_over")





# def play_game(user:str, computer:str):
#     '''this function plays the rock paper scissors game with the rules that:
#         scissors wins paper
#         rock with scissors
#         papper with rocks.
#     rock is represented as R
#     paper is represented as P
#     scissors is represented as S.

#     args:
#     user (str): this is the users choice.
#     computer(str): this is the computers choice

#     returns:
#         (str): this is the result of the game.
#     '''

    
#     if user == "S" and computer =="P":
#         return "YOU  WIN"
#     elif user== "P" and computer == "r":
#         return "YOU WIN"
#     elif user == "r" and computer =="s":
#         return "YOU WIN"
#     elif user== computer:
#         return"ITS A TIE"
#     else:
#         return "YOU LOSE"

# print("welcome to rock paper scissors game")
# print("enter R for rock, s for scissors nd p for paper")

# user= input("> ").lower()
# options= "rps"
# computer= random.choice(options)

# if user in options:
#     print(play_game(user, computer))

# else:
#     print("invalid input")

# print(computer)





# first_data= [5,3,32,2,27]
# second=[6,3,4,2,]

# zipped=





# arr= [28990, 566789,79087,6000]
# payraise= list(map(lambda x: x + (x*0.1), arr))
# print(payraise)



#classwork


#use of map command
# print("enter number seperate them by comma")
# str_num= input(">").split(",")
# mapped = list(map(int, str_num))

# print(sum(mapped)/ len(mapped))

#use of filter() command
# a= range(1,10)
# add= list(filter(lambda x: x % 2==1, a))
# print(add)

     
# myset={1,2,3,4,5,6,7,8,9}  
# # myset.remove(100)

# print(myset)

# myset.discard(3)
# myset.add(1000)




