math_mark = int(input("Enter the Math exam mark (0-100): "))
while math_mark < 0 or math_mark > 100:
    math_mark = int(input("Invalid input. Enter a valid Math mark (0-100): "))

english_mark = int(input("Enter the English exam mark (0-100): "))
while english_mark < 0 or english_mark > 100:
    english_mark = int(input("Invalid input. Enter a valid English mark (0-100): "))

ict_mark = int(input("Enter the ICT exam mark (0-100): "))
while ict_mark < 0 or ict_mark > 100:
    ict_mark = int(input("Invalid input. Enter a valid ICT mark (0-100): "))

average_mark = (math_mark + english_mark + ict_mark) / 3

print(f"Average mark: {average_mark}")

if average_mark >= 65:
    print("Pass")
else:
    print("Fail")
