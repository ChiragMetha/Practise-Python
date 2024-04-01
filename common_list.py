#write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
import random 
a = random.sample(range(1,50),10)
b = random.sample(range(1,50),14)
common_list = []

for x in a:
    if x in b and x not in common_list:
        common_list.append(x)
print(common_list)



