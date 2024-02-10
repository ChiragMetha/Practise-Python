# first and last number of a list is the same
# function to return True if the first and last number of a given list is same. If numbers are different then return False.
def first_last_num(numberlist):
    print("Given list:", numberlist)
    first_num = numberlist[0]
    last_num = numberlist[-1]
    
    if first_num == last_num:
        return True
    else:
        return False
number_x =[10, 20, 30, 40, 22]
print("Result is ", first_last_num(number_x))

number_y = [22, 41, 57, 62, 22]
print("Result is ", first_last_num(number_y))