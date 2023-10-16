# Set the minimum and maximum values
min_value = 1
max_value = 100

attempts = 0

while attempts < 3:
    try:
        user_input = int(input(f"Enter an integer between {min_value} and {max_value}: "))
        
        if min_value <= user_input <= max_value:
            print(f"Valid input: {user_input}")
            break
        else:
            print("Input is outside the valid range.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
    
    attempts += 1

if attempts == 3:
    print("None")
