import random

s = "abcdefghijklmnopqrstuvwxyz01234567890!@#$%^&*"
passlen = 6
passwords = "".join(random.sample(s,passlen))
print(f"# {passwords} #")