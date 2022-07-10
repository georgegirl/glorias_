# word= ("lacuna, peacemaker, woman, gloria, indomie")
# peacemaker
# woman
# gloria
# indomie
# lacuna
from ast import Not
from multiprocessing import RLock
import random
word_list = []
word_file = open("fifthclass.py/exercise.txt")
for word in word_file:
    word_list.append(word.strip())
answer= random.choice(word_list)
word= answer
tries_count= 0
tries = 4
display= "-"*len(answer)
n= 0
game_over= False
print(" WELCOME GAMER")
print("GAME STARTS NOW")
print("choose from below")
print("abcdefghijklmnopqrstuvwxyz")
print(answer)


while not game_over: #and tries != word
    print("YOU HAVE" + " " + str (tries) + " "  +"TRIES" +  " " + "REMAINING" )
    print(display)
    guess= input("ENTER WORD ")
    
    if guess in word:
        while word.find(guess, n) != -1:
           n = word.find(guess, n)
           display = display[:n] + guess + display[n + 1:]
           n += 1
        print("correct")
    else:
        print("wrong guess.")
        tries -= 1  
    if tries == 0:
        print("SORRY ATTEMPT USED UP")
        game_over= True

    if word== display:
       print("YOU WIN! THE WORD WAS  " + word)
       game_over= True  
    


    # if tries_count < tries:
    #     print(display)
    #     game_over = True


#     if guess in word:
#         i= word.find(guess)
#         display= display[ :i] + guess + display[i + 1:]
# print("YOU WIN")
# from multiprocessing import parent_process
