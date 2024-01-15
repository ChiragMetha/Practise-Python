# To find area of triangle
a = 5
b = 7
c = 8
#using semiperimeter formula finded s
s = (a+b+c)/2
#formula to find semiperimeter is (s*(s-a)(s-b)(s-c))**0.5
Area_of_traingle = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(f"The area of triangle is {Area_of_traingle}")