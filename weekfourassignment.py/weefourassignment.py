
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


        

