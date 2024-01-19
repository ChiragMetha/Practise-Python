# fibonaci series using while loop
nterm = int(input("Enter a  number for fibonacci sequence :  "))
n1 , n2 = 0 , 1
count = 0
if nterm <= 0:
    print("Enter a  positive integer")
elif nterm == 1:
    print(f"The fibonaci sequence for nterm 1 is {n1}")
else:
    print("The fibonaci sequence is: ")
    while count < nterm:
        print(n1)
        nth = n1 + n2
        n1 = n2 
        n2 = nth
        count +=  1