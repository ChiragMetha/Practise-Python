punctutions = '''!()-[]{ };:'"\,<>./?@#$%^&*_~'''
my_str = "Hello!!!,  he  said --- and  went."
pun_tation = ""
for char in my_str:
    if char not in punctutions:
        pun_tation = pun_tation + char
print(pun_tation)