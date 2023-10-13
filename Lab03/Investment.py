initial_investment = 100
target_value = 1000
interest_rate = 0.10  # 10%

years = 0

while initial_investment < target_value:
    initial_investment *= (1 + interest_rate)
    years += 1

print(f"It will take {years} years for the initial investment to grow to £1000.")
