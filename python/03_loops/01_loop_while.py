#!/usr/bin/env python3

## 01 - While Loop

# Loop only one condition
count = 0
while count < 5:
    print("Contador es:", count)
    count += 1  # Increment count to avoid infinite loop


# Loop with break and continue
number = 0
while number <= 5:
    number += 1
    if number == 3:
        continue  # Skip the rest of the loop when number is 3
    if number == 5:
        break  # Exit the loop when number is 5
    print("Número es:", number)


# Warning => Infinite Loop Example (commented out to prevent execution)
while True:
    print("Bucle infinito Presiona Control + C para detenerlo.")
