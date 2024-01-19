terms = int(input("Enter a number for power "))
result = list(map(lambda x: 2 ** x, range(terms)))
for i in range(terms):
    print(f"2 raised to power {i} is {result[i]}")