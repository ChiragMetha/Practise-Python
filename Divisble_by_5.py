# Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 
'''Expected Output:
Given list is  [10, 20, 33, 46, 55]
Divisible by 5
10
20
55'''
list = [10, 20, 33, 46, 55]
print("Given list is",list)
print("Divisble by 5 are: ") 
for num in list:
    if num % 5 == 0:       
        print(num)