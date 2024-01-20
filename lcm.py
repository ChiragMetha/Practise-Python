def computelcm(x, y):
    if x>y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater%x == 0) and (greater%y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm
num1 = 12
num2 = 24

print(f"The LCM of {num1, num2} is {computelcm(num1, num2)} ")
