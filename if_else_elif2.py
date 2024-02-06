"""A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade"""
Marks = int(input("Enter your marks for grading "))
if Marks>=80:
    print(Marks,"marks and got A grade")
elif Marks in range(60,81):
    print(Marks ,"marks and got B grade")
elif Marks in range(50,61):
    print(Marks ,"marks and got C grade")
elif Marks in range(45,51):
    print(Marks ,"marks and got D grade")
elif Marks in range(25,46):
    print(Marks ,"marks and got E grade")
else:
    print(Marks ,"marks and got F grade")