# accessing list 
list = ['banana','apple','mango']
print(list[1])

# list length 
list = ['banana','apple','mango','orange','pineapple']
print(len(list))

# list slicing
list = ['banana','apple','mango','orange','pineapple']
print(list[1:4])

# append element to list
list = ['banana','apple','mango','orange','pineapple']
list.append('Watermelon')
print(list)

# insert element to list
list = ['banana','apple','mango','orange','pineapple']
list.insert(2,"strawberry")
print(list)

# remove element from list
list = ['banana','apple','mango','orange','pineapple']
list.remove('apple')
print(list)

# checl existence in list
list = ['banana','apple','mango','orange','pineapple']
print("apple" in list)