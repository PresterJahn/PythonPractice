# Get and validate monthly investment
while (monthly_investment := float(input("Enter a monthly investment amount: "))) <= 0:
    print("Error: investment must be a positive number")

# Get and validate yearly interest rate
while (yearly_interest_rate := float(input("Enter a yearly interest rate: "))) <= 0:
    print("Error: yearly interest rate must be a positive number")

# Get and validate investment years
while (investment_years := int(input("Enter how many years to invest: "))) <= 0:
    print("Error: investment period must be a positive number of years")

monthly_interest_rate = yearly_interest_rate / 100 / 12
total_months = investment_years * 12
total_revenue = 0

# Calculate investment month by month
for month in range(1, total_months + 1):
    total_revenue = (total_revenue + monthly_investment) * (1 + monthly_interest_rate)
    print(f"Month {month} revenue: {total_revenue}")

# Display final result
print(f"After {investment_years} years, you will receive a total investment revenue of {total_revenue:,.2f} at a yearly rate of {yearly_interest_rate}")