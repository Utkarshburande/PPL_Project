import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (use correct path if needed)
data = pd.read_csv(r"recruitment_data.csv")

companies = data['company']
recruitments = data['recruitments']

# -------------------------------
# a) Bar Chart
# -------------------------------
plt.figure()
plt.bar(companies, recruitments)
plt.title("New Recruitments in Companies")
plt.xlabel("Companies")
plt.ylabel("Number of Recruitments")
plt.xticks(rotation=45)
plt.show()


# -------------------------------
# b) Pie Chart
# -------------------------------
plt.figure()
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
plt.title("Recruitment Distribution")
plt.show()


# -------------------------------
# c) Customized Pie Chart
# -------------------------------
explode = [0, 0.1, 0, 0, 0, 0, 0, 0]  # Highlight Google

plt.figure()
plt.pie(recruitments, labels=companies, autopct='%1.1f%%',
        explode=explode, shadow=True)
plt.title("Customized Pie Chart (Google Highlighted)")
plt.show()


# -------------------------------
# d) Doughnut Chart
# -------------------------------
plt.figure()
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
centre_circle = plt.Circle((0, 0), 0.5)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title("Doughnut Chart of Recruitments")
plt.show()


# -------------------------------------------
# Comparison: IBM vs Amdocs
# -------------------------------------------
ibm = data[data['company'] == 'IBM']['recruitments'].values[0]
amdocs = data[data['company'] == 'Amdocs']['recruitments'].values[0]

plt.figure()
plt.bar(['IBM', 'Amdocs'], [ibm, amdocs])
plt.title("Comparison: IBM vs Amdocs Recruitment")
plt.ylabel("Number of Recruitments")
plt.show()