# Input initial investment, target value, and interest rate
initial_investment = float(input("Enter the initial investment: £"))
target_value = float(input("Enter the target value: £"))
interest_rate = float(input("Enter the interest rate (as a decimal, e.g., 0.10 for 10%): "))

years = 0

while initial_investment < target_value:
    initial_investment *= (1 + interest_rate)
    years += 1

print(f"It will take {years} years for the initial investment to grow to £{target_value}.")
