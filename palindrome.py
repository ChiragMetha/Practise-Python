#palindrome means when u read a string reverse or by normal it give the same word
my_str = 'aIbohPhoBiA'
my_str = my_str.casefold()
rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
    print("The string is palindrome.")
else:
    print("The string is not palindrome.")