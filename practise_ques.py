# Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
num = int(input("Enter a number..."))
while num > 0:
    digit = num % 10 # gettin last digit first
    num = num // 10 # removing last digit and repeating a loop
    print(digit, end = " ")