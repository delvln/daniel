while True:
    str = input("Please enter a string (type 'done' to exit): ")
    if str.lower() == 'done':
        break
    remove = [',', '.', ':', '!', '?']
    for char in remove:
        str = str.replace(char, '')
    str = str.upper()
    print(str)

print("Bye !")