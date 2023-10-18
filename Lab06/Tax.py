def getIncomeTax(salary):
    personal_allowance = 11850
    basic_rate_limit = 34500
    higher_rate_limit = 150000
    tax_rate_basic = 0.2
    tax_rate_higher = 0.4
    tax_rate_additional = 0.45

    if salary <= personal_allowance:
        return 0
    elif salary <= basic_rate_limit:
        return (salary - personal_allowance) * tax_rate_basic
    elif salary <= higher_rate_limit:
        basic_tax = (basic_rate_limit - personal_allowance) * tax_rate_basic
        return basic_tax + (salary - basic_rate_limit) * tax_rate_higher
    else:
        basic_tax = (basic_rate_limit - personal_allowance) * tax_rate_basic
        higher_tax = (higher_rate_limit - basic_rate_limit) * tax_rate_higher
        return basic_tax + higher_tax + (salary - higher_rate_limit) * tax_rate_additional

salary1 = 25000
tax1 = getIncomeTax(salary1)
print(f"For a salary of £{salary1}, the income tax is £{tax1:.2f}")

salary2 = 50000
tax2 = getIncomeTax(salary2)
print(f"For a salary of £{salary2}, the income tax is £{tax2:.2f}")

salary3 = 200000
tax3 = getIncomeTax(salary3)
print(f"For a salary of £{salary3}, the income tax is £{tax3:.2f}")
