mylist = [12,2,23,16,8,7,9,13]
result = list(filter(lambda x: (x%2 == 0), mylist))
print(f"Number divisble by 2 is {result}")