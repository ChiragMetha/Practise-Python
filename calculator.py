def Add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def Divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.subtract")
print("3.multiply")
print("4.Divide")

while(True):
    choice = input("Enter choice(1/2/3/4) :")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter a number "))
            num2 = float(input("Enter a number "))
        except ValueError:
            print("Invalid Error")
            continue
        if choice == '1':
            print(num1, "+", num2, "=", Add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", Divide(num1, num2))
        
        nextcalculation = input("Do u want to do next calculation(yes/no)")
        if nextcalculation == "no":
            break
        else:
            print("Invalid Input")