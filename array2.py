# sorting
list = [1,5,19,87,24,3,54,16,8,24,79]
list.sort()
print((list))

# list concatenation
list1 = [1, 3, 5]
list2 = [2, 4, 6]
list3 = list1 + list2
list3.sort()
print(list3)

# using for loop
list1 = [2, 7, 5]
list2 = [3, 4, 6]
list3 = []
for item in list1:
    list3.append(item)
for element in list2:
    list3.append(element)
list3.sort()
print(list3)