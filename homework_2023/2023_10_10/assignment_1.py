while True:
    str = input("Please enter two words : ")
    if str.lower() == 'done':
        break
    words = str.split()
    if len(words) == 0:
        break
    elif len(words) == 2:
        w1, w2 = words[0], words[1]
        if w1 < w2:
            print(w1, "comes first")
        elif w2 < w1:
            print(w2, "comes first")
        else:
            print("Both words are equal", w1)
    else:
        print("Please enter in correct way")
print("-- bye !!")