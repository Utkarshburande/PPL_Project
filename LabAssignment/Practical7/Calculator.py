def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b
def mod(a, b): return a % b

while True:
    print("\n1.Add 2.Sub 3.Mul 4.Div 5.Mod 6.Exit")
    ch = int(input("Enter choice: "))
    
    if ch == 6:
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if ch == 1: print(add(a,b))
    elif ch == 2: print(sub(a,b))
    elif ch == 3: print(mul(a,b))
    elif ch == 4: print(div(a,b))
    elif ch == 5: print(mod(a,b))
