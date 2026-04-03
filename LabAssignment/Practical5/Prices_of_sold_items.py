prices = tuple(map(int, input("Enter prices: ").split()))

print("Total items sold:", len(prices))
print("Cheapest:", min(prices))
print("Costliest:", max(prices))
print("Sorted:", sorted(prices))
print("Count of costliest:", prices.count(max(prices)))