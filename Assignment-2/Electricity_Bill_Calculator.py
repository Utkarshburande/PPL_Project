# Program to calculate electric bill based on units consumed
customer_num = input("Enter Customer Number: ")
units = float(input("Enter Power Consumed (Units): "))

# Calculate amount based on the provided table
if units <= 100:
    amount = units * 1.00
elif units <= 300:
    # Rs. 100 for first 100 units + 1.25 for units over 100
    amount = 100 + (units - 100) * 1.25
elif units <= 500:
    # Rs. 350 for first 300 units + 1.50 for units over 300
    amount = 350 + (units - 300) * 1.50
else:
    # Rs. 650 for first 500 units + 1.75 for units over 500
    amount = 650 + (units - 500) * 1.75

# Output well-formatted
print("-" * 30)
print(f"ELECTRICITY BILL")
print("-" * 30)
print(f"Customer Number : {customer_num}")
print(f"Units Consumed  : {units}")
print(f"Total Payable   : Rs. {amount:.2f}")
print("-" * 30)