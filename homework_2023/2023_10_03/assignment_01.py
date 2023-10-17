def calc(score):
    if  score < 0 or score > 100:
        return ("Error, please enter numeric input between 0 and 100")
    elif score >= 90:
        return("Grade is A")
    elif score >= 80:
        return("Grade is B")
    elif score >= 70:
        return("Grade is C")
    elif score >= 60:
        return("Grade is D")
    else:
        return("Grade is F")
try:
    score_input = float(input("Enter score: "))
    grade = calc(score_input)
    print(f"{grade}")
except ValueError:
    print("Error: please enter a valid numeric score between 0 and 100")