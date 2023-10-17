def computepay(hours, rate):
    if hours > 40:
       salary = 40 * rate + ((hours - 40) * rate * 1.5)
    else:
        salary = hours * rate
    return salary
try:
    hours = int(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    if hours < 0 or rate < 0:
        print("Wrong input")
    else:
        pay = computepay(hours, rate)
        print(f"Salary: {pay:.1f}")
except ValueError:
    print("Error, please enter numeric input")