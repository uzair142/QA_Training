flavours = {"Banana": 1, "Strawberry": 2, "Mango": 3, "Guava": 4}
budget = int(input("What is your budget? £"))

while True:
    print(f"\nHi there, you have £{budget} left. What can we get for you?")
    print("Please take a look at our menu:")
    for flavor, price in flavours.items():
        print(f"{flavor}: £{price}")
    print("Alternatively, type 'Q' to leave.")
    
    decision = input("Enter your choice: ").strip().capitalize()

    if decision == 'Q':
        break
    elif decision in flavours:
        price = flavours[decision]
        if budget >= price:
            budget -= price
            print(f"Here's your {decision} milkshake. You now have £{budget} left.")
        else:
            print("Sorry, you don't have enough budget for that flavor.")
    else:
        print("That is not a valid flavor. Please choose from the menu.")
