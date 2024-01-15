import cmath #its a library that does complex maths
#formula to find quadratic equation is -b+-(b**2)-(4*a*c)/(2*a)
a = 5
b = 10
c = 15
#first solving determinant
d =  (b**2)-(4*a*c)
sol1 = -b-cmath.sqrt(d)/(2*a)
sol2 = -b+cmath.sqrt(d)/(2*a)

print(f"The solution of quadratic equation is{sol1},{sol2}")