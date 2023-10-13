print("Pythagoras' Calculator")
print("1. Find the length of A given B and C")
print("2. Find the length of B given A and C")
print("3. Find the length of C given A and B")

choice = input("Enter your choice (1/2/3): ")

if choice == '1':
    b = float(input("Enter the length of side B: "))
    c = float(input("Enter the length of side C: "))
    a = (c**2 - b**2)**0.5
    print(f"The length of side A is {a}")
    
elif choice == '2':
    a = float(input("Enter the length of side A: "))
    c = float(input("Enter the length of side C: "))
    b = (c**2 - a**2)**0.5
    print(f"The length of side B is {b}")
    
elif choice == '3':
    a = float(input("Enter the length of side A: "))
    b = float(input("Enter the length of side B: "))
    c = (a**2 + b**2)**0.5
    print(f"The length of side C is {c}")

else:
    print("Invalid choice. Please enter 1, 2, or 3 to perform the corresponding calculation.")
