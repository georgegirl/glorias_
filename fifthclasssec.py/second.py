
import statistics
num_of_terms = int(input("how many values you add in the list"))
sample_list = []
counter = 1
while num_of_terms >= counter:
    user_input  = int(input("enter the value  = "))
    sample_list.append(user_input)
    counter = counter + 1


mean = statistics.mean(sample_list)

median = statistics.median(sample_list)

mode= statistics.mode(sample_list)

Variance= round ((sum((x - mean) ** 2 for x in sample_list) / num_of_terms),3)

standard_d = round(statistics.sqrt(Variance),3)





with open("classworkfile.py.txt", "w") as f:
    f.write(f"standard_d: {standard_d }\n Variance: {Variance}\n median: {median}\n mean: {mean}\n mode:{mode} ")




    