try:
    file_name = input("Enter a file name: ")
    with open(file_name, 'r') as file:
        for line in file:
            print(line.upper())


except FileNotFoundError:
    print("Error, file doesn't exist")