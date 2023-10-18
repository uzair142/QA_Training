# Input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display the calculator menu
print("Calculator Menu:")
print("1. Add +")
print("2. Subtract -")
print("3. Multiply *")
print("4. Divide /")
print("5. Square s")


choice = input("Choose an operation (1/2/3/4/5): ")


if choice == '1':
    result = num1 + num2
elif choice == '2':
    result = num1 - num2
elif choice == '3':
    result = num1 * num2
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."
elif choice == '5':
    result1 = num1 * num1
    result2 = num2 * num2
else:
    result = "Invalid choice. Please select a valid operation (1/2/3/4/5)."

# Print the result
print("Result:", result)
