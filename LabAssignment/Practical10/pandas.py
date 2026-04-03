import pandas as pd

# Creating data for 5 states
data = {
    "State": ["Maharashtra", "Gujarat", "Rajasthan", "Uttar Pradesh", "Madhya Pradesh"],
    "Area (sq km)": [307713, 196024, 342239, 240928, 308245],
    "Population": [124000000, 70000000, 81000000, 240000000, 85000000]
}

# Creating DataFrame
df = pd.DataFrame(data)

# a) Print complete information
print("\n--- Complete Information of States ---")
print(df)

# b) State with largest Area
largest_area_state = df.loc[df["Area (sq km)"].idxmax()]
print("\nState with Largest Area:", largest_area_state["State"])

# c) State with largest Population
largest_population_state = df.loc[df["Population"].idxmax()]
print("State with Largest Population:", largest_population_state["State"])

# d) Calculate Population Density
df["Population Density"] = df["Population"] / df["Area (sq km)"]

print("\n--- Population Density of States ---")
print(df[["State", "Population Density"]])

# e) State with highest Population Density
highest_density_state = df.loc[df["Population Density"].idxmax()]
print("\nState with Highest Population Density:", highest_density_state["State"])