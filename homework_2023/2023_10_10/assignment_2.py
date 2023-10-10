str = input("Enter a string: ")
print("Input string:", str)
index = len(str) - 1

while index >= 0:
    print(str[index], "\n")
    index -= 1