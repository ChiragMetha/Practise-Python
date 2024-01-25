my_str = "Hello this Is an Example With cased letters"
my_str = my_str.split()
words = [word.lower() for word in my_str]
words.sort()
print("The sorted words are:")
for word in words:
    print(word)