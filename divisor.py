#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. If you don’t know what a divisor is, it is a number that divides evenly into another number. 
number = int(input("Enter a number foor divisor: "))
listrange = list(range(1,number+1))
divisor = []
for num in listrange:
    if number % num == 0:
        divisor.append(num)
print(divisor)