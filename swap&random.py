#Swap two variables without using third variable
a = 5
b = 6
a = a + b
b = a - b
a = a - b
print(a)
print(b)
#swapping two variables using 3 variable
c = 10
d = 15
Temp = c
c = d
d = Temp
print(c)
print(d) 

#Random Number
from random import randint
print(randint(1,7))