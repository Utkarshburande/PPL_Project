# --- Lab Assignment 2 ---
# Program to generate Annual Purchase/Billing report for a Vendor

# 1. Store Vendor Details
v_name = input("Enter Vendor Name: ")
v_year = input("Year of Association: ")
v_contact = input("Contact Number: ")
v_email = input("Email ID: ")

# 2. Read Monthly Purchases
monthly_purchases = []
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

print("\nEnter purchase amounts for each month:")
for month in months:
    amount = float(input(f"Amount for {month}: "))
    monthly_purchases.append(amount)

# 3. Calculate Totals
total_annual = sum(monthly_purchases)
avg_monthly = total_annual / 12

# 4. Generate Annual Purchase Report
print("\n" + "*"*45)
print(f"{'ANNUAL PURCHASE REPORT':^45}")
print("*"*45)
print(f"Vendor: {v_name}")
print(f"Since:  {v_year}")
print(f"Contact: {v_contact} | Email: {v_email}")
print("-" * 45)

# Print a simplified table of monthly data
print(f"{'Month':<15} | {'Purchase Amount':>20}")
print("-" * 45)
for i in range(12):
    print(f"{months[i]:<15} | Rs. {monthly_purchases[i]:>17,.2f}")

print("-" * 45)
print(f"TOTAL ANNUAL BILLING: Rs. {total_annual:,.2f}")
print(f"AVERAGE MONTHLY SPEND: Rs. {avg_monthly:,.2f}")
print("*"*45)