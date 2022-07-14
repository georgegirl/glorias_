#FUNCTIONS TO CALCULATE THE FOLLOWING STATISTICAL MEASURES:
#MEAN------- QUESTION 1

from math import sqrt


x = [50,50,78,34,100,50,60,12,60]
x.sort()
print(x)
def mean(x):
    total= 0
    for num in x:
        total = total + num
    return int(total / len(x))

print(mean(x))


#QUESTION 2 MEDIAN
def median(x):
    x.sort()
    n = len(x)//2
    if len(x) % 2 != 0: 
        return x[n]
    elif len(x) % 2 == 0:
        return ((x [n - 1] + x[n]) / 2)


print(median(x))


#QUESTION 3 VARIANCE