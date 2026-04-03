balance = 0

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
    else:
        print("Insufficient balance")

while True:
    print("\n1.Check Balance 2.Deposit 3.Withdraw 4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        print("Balance:", balance)
    elif ch == 2:
        amt = float(input("Enter amount: "))
        deposit(amt)
    elif ch == 3:
        amt = float(input("Enter amount: "))
        withdraw(amt)
    else:
        break
