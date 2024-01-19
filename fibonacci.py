# fibonacci series using for loop
a = 0
b = 1
series_length = int(input("Enter a series length of series "))
print(a, b, end=' ')
for i in range(series_length):
    c = a + b
    print(c, end= ' ')
    a = b
    b = c 