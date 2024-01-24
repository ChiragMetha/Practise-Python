def recur_binary(x):
    if x > 1:
        recur_binary(x // 2)
    print(x % 2, end = ' ')

decimal = int(input("Enter a number "))
recur_binary(decimal)
print()
        