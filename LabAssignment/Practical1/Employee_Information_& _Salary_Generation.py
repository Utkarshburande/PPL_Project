# --- Lab Assignment 1 ---
# Program to calculate Employee Salary

# 1. Input Employee Details
emp_name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
dept = input("Enter Department: ")
basic_salary = float(input("Enter Basic Salary: "))

# 2. Salary Calculations
# DA is 92% of Basic
da = basic_salary * 0.92
# HRA is 58% of Basic
hra = basic_salary * 0.58
# TA is 30% of Basic
ta = basic_salary * 0.30
# Fixed Deduction
lic = 500

# Gross Salary = Basic + Allowances
gross_salary = basic_salary + da + hra + ta
# Net Salary = Gross - Deductions
net_salary = gross_salary - lic

# 3. Generate Salary Slip
print("\n" + "="*40)
print(f"{'SALARY SLIP':^40}")
print("="*40)
print(f"Name: {emp_name:<20} ID: {emp_id}")
print(f"Dept: {dept}")
print("-" * 40)
print(f"Basic Salary: Rs. {basic_salary:,.2f}")
print(f"DA (92%):     Rs. {da:,.2f}")
print(f"HRA (58%):    Rs. {hra:,.2f}")
print(f"TA (30%):     Rs. {ta:,.2f}")
print("-" * 40)
print(f"Gross Salary: Rs. {gross_salary:,.2f}")
print(f"LIC Deduction:Rs. {lic:,.2f}")
print("-" * 40)
print(f"NET SALARY:   Rs. {net_salary:,.2f}")
print("="*40)