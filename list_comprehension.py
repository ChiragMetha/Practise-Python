# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
a = [12,14,125,784,1269,14,7,1475,1542,1201,320,333]
ages = []
for age in a:
    ages.append(2024-age)
print(ages)

# for one line code
years = [2012,2014,2016,2018,2022,2023]
age = [2024-age for age in years]
print(age)