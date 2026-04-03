# --- Lab Assignment 1 ---
# a) Calculate Current using Ohm's Law (I = V / R)

try:
    voltage = float(input("Enter Voltage (V): "))
    resistance = float(input("Enter Resistance (R): "))

    # Calculate Current
    if resistance == 0:
        print("Error: Resistance cannot be zero.")
    else:
        current = voltage / resistance
        print(f"Calculated Current: {current:.2f} A")

        # b) Display the nature of current
        if current < 0.5:
            print("Nature of Current: Low current")
        elif 0.5 <= current <= 2:
            print("Nature of Current: Normal current")
        else: # current > 2
            print("Nature of Current: High current")

except ValueError:
    print("Invalid input. Please enter numerical values.")