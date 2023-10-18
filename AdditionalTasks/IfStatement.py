a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

largest = a  

if b > largest:
    largest = b
if c > largest:
    largest = c

if largest % 2 == 0:
    print("Even Number")
elif largest % 3 == 0:
    print("Odd Number and a Multiple of 3")
else:
    print("Odd Number")
