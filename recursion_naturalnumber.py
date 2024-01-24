def recu_num(x):
    if x<=1:
        return x
    else:
        return x + recu_num(x-1)
num = int(input("enter a number "))
if num < 0:
    print("Enter a positive number ")
else:
    print(f"The recursion of {num} is {recu_num(num)}")