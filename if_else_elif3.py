'''Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
if employee is female, then she will work only in urban areas.

if employee is a male and age is in between 20 to 40 then he may work in anywhere

if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

And any other input of age should print "ERROR".'''
user = int(input("Enter your age "))
Status = input(" Marital status? (yes/no) ")
Gender = input(" Sex (M or F) ")
if Gender == "F" and user in range(20,41):
    print("She will work in urban areas.")
elif Gender == "M" and user in range(20,41):
    print("He can work anywhere.")
elif Gender == "M" and user in range(40,61):
    print("He will work in urban areas only.")
else:
    print("Error.....")