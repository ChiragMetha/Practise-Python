Num1 = 6
Num2 = 10
Num3 = 8
if (Num1 >= Num2) and (Num1 >= Num3):
    largest = Num1
elif (Num2 >= Num1) and (Num2 >= Num3):
    largest = Num2
else:
    largest = Num3
    
print(f"The largest Number is {largest}")