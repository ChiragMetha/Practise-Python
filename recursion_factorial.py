def  recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n-1)
num = int(input("Enter a number for  factorial "))
if num < 0 :
    print("Sorry u cant put a negative number ")
elif num == 0:
    print("factorial of num 0 is 1")
else:
    print(f"The recursion of factorial number {num} is {recur_factorial(num)} ")