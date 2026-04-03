import pandas as pd

# Load CSV file
df = pd.read_csv("books.csv")

# a) Print complete report
def print_all_books():
    print("\n--- Complete Book Report ---")
    print(df.to_string(index=False))


# b) Books by given author
def books_by_author(author_name):
    result = df[df['Author'].str.lower() == author_name.lower()]
    
    print(f"\n--- Books by Author: {author_name} ---")
    if result.empty:
        print("No books found.")
    else:
        print(result.to_string(index=False))


# c) Books by given publisher
def books_by_publisher(publisher_name):
    result = df[df['Publisher'].str.lower() == publisher_name.lower()]
    
    print(f"\n--- Books by Publisher: {publisher_name} ---")
    if result.empty:
        print("No books found.")
    else:
        print(result.to_string(index=False))


# d) Cheapest and Costliest book
def cheapest_costliest():
    min_price = df['Price'].min()
    max_price = df['Price'].max()

    cheapest = df[df['Price'] == min_price]
    costliest = df[df['Price'] == max_price]

    print("\n--- Cheapest Book ---")
    print(cheapest.to_string(index=False))

    print("\n--- Costliest Book ---")
    print(costliest.to_string(index=False))


# e) Sort by year
def sort_by_year():
    sorted_df = df.sort_values(by='Year')
    
    print("\n--- Books Sorted by Year ---")
    print(sorted_df.to_string(index=False))


# ===== MENU DRIVEN PROGRAM =====
while True:
    print("\n===== BOOK MANAGEMENT SYSTEM =====")
    print("1. Show all books")
    print("2. Search books by author")
    print("3. Search books by publisher")
    print("4. Cheapest & Costliest book")
    print("5. Sort books by year")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print_all_books()

    elif choice == '2':
        author = input("Enter author name: ")
        books_by_author(author)

    elif choice == '3':
        publisher = input("Enter publisher name: ")
        books_by_publisher(publisher)

    elif choice == '4':
        cheapest_costliest()

    elif choice == '5':
        sort_by_year()

    elif choice == '6':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")