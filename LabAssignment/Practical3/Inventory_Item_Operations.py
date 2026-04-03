# Initial list setup
item_str = input("Enter item numbers separated by spaces: ")
items = [int(x) for x in item_str.split()]

# a) Total number of items
print(f"a) Total items: {len(items)}")

# b) Last item in the list
if items:
    print(f"b) Last item: {items[-1]}")

# c) Sorted list
print(f"c) Sorted list: {sorted(items)}")

# d) Search for item 515
if 515 in items:
    print("d) Yes (515 exists)")
else:
    print("d) No")

# e) Add 121 and 321, then sort and print
items.extend([121, 321])
items.sort()
print(f"e) Updated and sorted list: {items}")