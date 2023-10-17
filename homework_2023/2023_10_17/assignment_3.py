try:
    file_input = input("Enter a file name: ")
    counter = 0
    total = 0

    with open(file_input, 'r') as file:
        for line in file:
            if line.startswith("X-DSPAM-Confidence:"):
                try:
                    confidence = float(line.split(":")[1].strip())
                    total += confidence
                    count += 1
                except ValueError:
                    continue

    if count > 0:
        average = total / count
        print(f"Average spam confidence: {average:.14f}")


except FileNotFoundError:
    print("File cannot be opened")