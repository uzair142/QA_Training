while True:
    print("Time Calculator")
    print("1- Add 2 times")
    print("2- Find the difference between 2 times")
    print("3- Convert to Hours")
    print("4- Convert to Minutes")
    print("5- Convert Minutes to Time")
    print("6- Convert Hours to Time")
    print("7- Convert Days to Time")
    print("8- Exit")

    option = input("Enter an option: ")

    if option == "1":
        time1 = input("Enter the first time (DD:HH:MM): ")
        time2 = input("Enter the second time (DD:HH:MM): ")
        
        # Parse time1
        days1, hours1, minutes1 = map(int, time1.split(":"))
        
        # Parse time2
        days2, hours2, minutes2 = map(int, time2.split(":"))
        
        # Add the times
        total_minutes = (days1 + days2) * 24 * 60 + (hours1 + hours2) * 60 + minutes1 + minutes2
        
        # Calculate days, hours, and minutes
        days, total_minutes = divmod(total_minutes, 24 * 60)
        hours, minutes = divmod(total_minutes, 60)
        
        result = f"Result: {days:02d}:{hours:02d}:{minutes:02d}"
        print(result)

    elif option == "2":
        time1 = input("Enter the first time (DD:HH:MM): ")
        time2 = input("Enter the second time (DD:HH:MM): ")
        
        # Parse time1
        days1, hours1, minutes1 = map(int, time1.split(":"))
        
        # Parse time2
        days2, hours2, minutes2 = map(int, time2.split(":"))
        
        # Calculate the absolute difference in minutes
        total_minutes1 = days1 * 24 * 60 + hours1 * 60 + minutes1
        total_minutes2 = days2 * 24 * 60 + hours2 * 60 + minutes2
        difference_minutes = abs(total_minutes1 - total_minutes2)
        
        # Calculate days, hours, and minutes for the difference
        days, difference_minutes = divmod(difference_minutes, 24 * 60)
        hours, minutes = divmod(difference_minutes, 60)
        
        result = f"Difference: {days:02d}:{hours:02d}:{minutes:02d}"
        print(result)

    elif option == "3":
        time = input("Enter the time (DD:HH:MM): ")
        
        # Parse time
        days, hours, minutes = map(int, time.split(":"))
        
        # Convert to hours
        total_hours = days * 24 + hours + minutes / 60
        result = f"Hours: {total_hours:.2f}"
        print(result)

    elif option == "4":
        time = input("Enter the time (DD:HH:MM): ")
        
        # Parse time
        days, hours, minutes = map(int, time.split(":"))
        
        # Convert to minutes
        total_minutes = days * 24 * 60 + hours * 60 + minutes
        result = f"Minutes: {total_minutes}"
        print(result)

    elif option == "5":
        minutes = int(input("Enter the number of minutes: "))
        
        # Convert minutes to days, hours, and minutes
        days, minutes = divmod(minutes, 24 * 60)
        hours, minutes = divmod(minutes, 60)
        result = f"Time: {days:02d}:{hours:02d}:{minutes:02d}"
        print(result)

    elif option == "6":
        hours = float(input("Enter the number of hours: "))
        
        # Split hours into days and remaining hours
        days, hours = divmod(hours, 24)
        
        # Calculate the remaining minutes
        remaining_minutes = hours * 60
        
        result = f"Time: {int(days):02d}:{int(remaining_minutes):02d}:00"
        print(result)

    elif option == "7":
        days = int(input("Enter the number of days: "))
        result = f"Time: {days:02d}:00:00"
        print(result)

    elif option == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please enter a valid option.")
