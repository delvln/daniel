str = input("PLease enter string :")

c_upper = 0
c_num = 0
c_lower = 0
c_other = 0

for char in str:
    if char.isdigit():
        c_num += 1
    elif char.isupper():
        c_upper += 1
    elif char.islower():
        c_lower += 1
    else:
        c_other += 1

print("-   Uppercase letters:", c_upper)
print("-   Lowercase letters:", c_lower)
print("-   Numbers:", c_num)
print("-   Other characters:", c_other)

