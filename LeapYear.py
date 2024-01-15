year = int(input("Enter a year "))
# divide by 400 to know its a leap year and divide byy 100 to knows is it in century year
if (year%400 == 0) and (year%100 == 0):
    print(f"The year {year} is a leap year")
# leap year is divisible by 4 and also not by 100 to know is it in century year
elif (year%4 == 0) and (year%100 != 0):
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is not a leap year")