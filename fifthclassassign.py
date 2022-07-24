from statistics import mode


my_list= [2,3,4,56,78,9,2,4,6,8,9,8,6,56,102,4,4,5,6,7,8,2,4,6,7,2,102,4,1,6,7,8,4,2,7,9]
k = [78,90,40,60,20,20,60,20,50,90,90,40,20,30,20]
my_list.sort()
occur={}

for items in my_list:
    if items in occur:
        occur[items] +=1
    else:
        occur[items] =1
for key, value in occur.items():
    print(key," : ", value)
    
sorted_item={key : value for (key, value) in sorted(occur.items(), 
key= lambda x: x[1], reverse= True)} 


print("Total for each list: " ,len(my_list), "|" , len(k))
print(sorted_item)
print("Top frequent element: ", list(sorted_item) [0] )
''' an alternative solution would be to get the mode of the given list
                by importing mode from the library statistics, using the finding mode to get the most fequent value
                i.e print(mode(my_list))'''

print("second most frequent element: ", list(sorted_item) [1] )
print("third most frquent element: ", list(sorted_item) [2] )   
print("Top frequency element in k: ", mode(k))
''' an alternative of this would be to give two parameters which provides the set of k 
                and each set being counted, then finding the maximum occurance of k. i.e
                print(max(set(k), key = k.count))'''



#EXPLANATION
''' gave an array of numbers titled "my_list" and an integer  "k"
then i used the sort() method to sort the list, created a dictionary titled "occur"
in order to save element as key and frequency as value.
I then issued a for loop that gives a restatement 
through the list with a condition that states,
if the element already exist in the list then give an addition to the element and
if the value doesn't have an addition then assign it the value of 1 
for the keys and value in occur, i then printed the elements as key, 
and the values as the amount of times it occured in the list.

To get the most occuring values in the dictionary in descending order:
with the specified dictionary "occur", i maintained count of the keys
by sorting based on the property of the key,
that is its value in dictionary "occur" providing a parameter and
using a lambda function to sort in a desending order thereby deriving
outputs that gives the highest occuring values in desending order''' 
