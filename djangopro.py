from turtle import *
from random import randrange
from math import square,vector



food = vector(0,0)
snake= [vector(10,0)]
aim = vector(0,-10)

def change(x,y):
    aim.x = x
    aim.y = y

def inside(head):
    return -200<head.x <190 and -200 <head.y <190

def move():
    head = snake[-1].copy()
    head.move(aim)



    if not inside(head) and head in snake:
        square(head.x,head.y,9,'red')
        update()
        return

    snake.append()



