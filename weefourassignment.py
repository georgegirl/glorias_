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

import statistics
num_of_terms = int(input("how many values you add in the list"))
sample_list = []
counter = 1
while num_of_terms >= counter:
    user_input  = int(input("enter the value  = "))
    sample_list.append(user_input)
    counter = counter + 1




mean = statistics.mean(sample_list)
print("mean of value is = ", mean)


median = statistics.median(sample_list)
print("median of the value = ", median)

Variance= sum((x - mean) ** 2 for x in sample_list) / num_of_terms
print("variance of values is = ",Variance)

standard_d = statistics.sqrt(Variance)
print("standard deviation of values is =", standard_d)


        

