t = tuple(map(int, input("Enter numbers: ").split()))

print("Total items:", len(t))
print("Last item:", t[-1])
print("Reverse:", t[::-1])
print("Yes" if 5 in t else "No")

new_t = t[1:-1]
sorted_t = tuple(sorted(new_t))
print("Updated tuple:", sorted_t)