mark = int(input("Enter the exam mark (between 1 and 100): "))

if 1 <= mark <= 100:
    if mark < 50:
        grade = "Fail"
    elif 50 <= mark <= 60:
        grade = "Pass"
    elif 61 <= mark <= 70:
        grade = "Merit"
    else:
        grade = "Distinction"
    
    
    print("Grade:", grade)
else:
    print("Error: Marks must be between 1 and 100.")
