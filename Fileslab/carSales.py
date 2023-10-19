companies = []
sales = []

with open("carSales.csv", "r") as file:
    lines = file.readlines()

for x in range(0, len(lines), 2):
    company_name = lines[x].strip()
    data = lines[x + 1].strip().split(',')
    sales_data = list(map(int, data))
    
    companies.append(company_name)
    sales.append(sales_data)

# Calculate the sum of cars sold in each month
print("Sum of cars sold in each month:")
monthly_totals = [sum(month_sales) for month_sales in zip(*sales)]
for month, total in zip(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"], monthly_totals):
    print(f"{month}: {total}")

# Calculate the total yearly sales by each manufacturer
print("\nTotal yearly sales by each manufacturer:")
yearly_totals = [sum(company_sales) for company_sales in sales]
for company, total in zip(companies, yearly_totals):
    print(f"{company}: {total}")

# Calculate and display the grand total
grand_total = sum(yearly_totals)
print("\nGrand total:", grand_total)
