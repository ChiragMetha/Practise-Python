num = int(input("Enter a Number "))
if num == 1:
    print(num, "Its not a prime number")
elif num > 1:
    for  i in range(2,num):
        if (num%i==0):
            print(num, "Its not a prime number")
            break
    else:
        print(num, "Its a Prime number.")
            