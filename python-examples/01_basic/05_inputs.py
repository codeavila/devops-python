#!/usr/bin/env python3

## 04 - Inputs

"""
This script demonstrates how to take user input in Python using the input() function.
It also shows how to handle different data types and perform basic operations with the input values.
"""

# Taking string input from the user
name = input("Ingrese su nombre: ", end="!\n")
print(f"Hola, {name}! Bienvenido a CodeCraftAvila.")

# Taking integer input from the user (you can end with a newline)
age = int(input("Ingrese su edad: \n"))
print(f"Tienes {age} años.")
# Taking float input from the user

height = float(input("Ingrese su altura en metros (por ejemplo, 1.75): ", end="!\n"))
print(f"Tu altura es {height} metros.")


"""
You can also input multiple values in one line and split them
using the split() method.
"""
# Taking multiple integer inputs from the user
num1, num2 = map(
    int, input("Ingrese dos números enteros separados por espacio: ").split()
)
sum_result = num1 + num2
print(f"La suma de {num1} y {num2} es {sum_result}.")

# Taking multiple name and last name inputs from the user
first_name, last_name = input(
    "Ingrese su nombre y apellido separados por espacio: "
).split()
print(f"Hola, {first_name} {last_name}! Encantado de conocerte.")
