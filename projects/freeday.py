import random
from re import T


word_list = ["goal", "mine", "hole", "long", "land","told", "boat", "dull", "word", "runs",
    "call", "bank", "dogs", "hang", "mail", "pole", "sail","time", "good",'wale', 'play']
com_choice = 'goal'
num_guess = 0
n = 0 
display = '_'*len(com_choice)
while True:  
    guess = input("INPUT LETTER: ").lower()
    while com_choice.find(guess, n) != -1:
       
        num_guess = com_choice.find(guess, n)
        n = com_choice.find(guess, n) #n represent the location of the letter guessed correctly in the word
        display1 = display[:n] + guess + display[n + 1:]
        display = display1
        print(display)
        n += 1
        if display == com_choice:
            break
