mark = int(input("Enter the exam mark (between 1 and 100): "))

if 1 <= mark <= 100:
    level = int(input("Enter the student level (1 or 2): "))

    if level == 1:
        if mark < 50:
            grade = "Fail"
        elif 50 <= mark <= 60:
            grade = "Pass"
        elif 61 <= mark <= 70:
            grade = "Merit"
        else:
            grade = "Distinction"
    elif level == 2:
        if mark < 40:
            grade = "Fail"
        elif 40 <= mark <= 50:
            grade = "Pass"
        elif 51 <= mark <= 65:
            grade = "Merit"
        else:
            grade = "Distinction"
    else:
        grade = "Error: Invalid student level. Please enter 1 or 2."
else:
    grade = "Error: Marks must be between 1 and 100."

print("Grade:", grade)
