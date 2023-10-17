def num_divide3(num):
    c = 0
    for i in range(1, num + 1):
        if i % 3 == 0:
            c += 1
    return c
while True:
    user_input = input("Enter a positive integer : ")
    if user_input == 'done':
        print("bye !!")
        break
    try:
        num = int(user_input)
        if num <= 0:
            print("please enter a positive number")
        else:
            result = num_divide3(num)
            print(f"numbers divisible by 3 among numbers from 1 to {num} is: {result}")
    except ValueError:
        print("please enter a positive number ")