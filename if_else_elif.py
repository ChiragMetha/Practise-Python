# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years,
# Ask user for their salary and year of service and print the net bonus amount.
salary = int(input("enter a salary "))
yos = int(input("enter a years of salary"))
if yos > 5:
    print("you got bonus",0.05*salary)
else:
    print(("No bonus"))