import pandas as pd
import matplotlib.pyplot as plt
import os

# Check current working directory
print("Current Working Directory:", os.getcwd())

# 👉 Use FULL PATH of your CSV file (change if needed)
data = pd.read_csv(r"C:\Users\vedan\OneDrive\Desktop\PPL_Assignment\sales_data.csv")

# -------------------------------
# a) Line Plot for Total Profit
# -------------------------------
plt.figure()
plt.plot(data['month_number'], data['total_profit'], marker='o')
plt.title("Total Profit of All Months")
plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.grid(True)
plt.show()


# ------------------------------------
# b) Multiline Plot for Product Sales
# ------------------------------------
plt.figure()

plt.plot(data['month_number'], data['facecream'], label='Face Cream')
plt.plot(data['month_number'], data['facewash'], label='Face Wash')
plt.plot(data['month_number'], data['toothpaste'], label='Toothpaste')
plt.plot(data['month_number'], data['bathingsoap'], label='Bathing Soap')
plt.plot(data['month_number'], data['shampoo'], label='Shampoo')
plt.plot(data['month_number'], data['moisturizer'], label='Moisturizer')

plt.xlabel("Month Number")
plt.ylabel("Sales Units")
plt.title("Sales Data of All Products")
plt.legend()
plt.grid(True)
plt.show()


# ------------------------------------
# c) Bar Chart for Face Cream & Wash
# ------------------------------------
plt.figure()

bar_width = 0.4
months = data['month_number']

plt.bar(months - bar_width/2, data['facecream'], width=bar_width, label='Face Cream')
plt.bar(months + bar_width/2, data['facewash'], width=bar_width, label='Face Wash')

plt.xlabel("Month Number")
plt.ylabel("Sales Units")
plt.title("Face Cream and Face Wash Sales Data")
plt.legend()
plt.show()


# ------------------------------------
# d) Pie Chart for Yearly Sales
# ------------------------------------
total_sales = [
    data['facecream'].sum(),
    data['facewash'].sum(),
    data['toothpaste'].sum(),
    data['bathingsoap'].sum(),
    data['shampoo'].sum(),
    data['moisturizer'].sum()
]

labels = ['Face Cream', 'Face Wash', 'Toothpaste', 'Bathing Soap', 'Shampoo', 'Moisturizer']

plt.figure()
plt.pie(total_sales, labels=labels, autopct='%1.1f%%')
plt.title("Total Yearly Sales Data for Each Product")
plt.show()