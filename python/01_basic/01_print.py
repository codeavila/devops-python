#!/usr/bin/env python3
## 01 - Print

## Basic print example in Python
print("Hola, Mundo by CodeCraftAvila")

## Only for documentation purposes
"""
This script demonstrates various ways to use the print function in Python.
"""

"""
Also for documentation purposes
using single quotes for multi-line comments.
"""

## Formatted print example
name = "CodeCraftAvila"
age = 35
print(f"Hola, soy {name} y tengo {age} años.")

## Multi-line print example
print(
    """Este es un ejemplo
de impresión
en múltiples líneas."""
)

## Concatenation example
print("Hola, " + name + ". Tienes " + str(age) + " años.")

## Separator and end parameters example
print("Python", "es", "genial", sep=" - ", end="!\n")
### sep parameter changes the separator between arguments
### end parameter changes what is printed at the end (default is newline)

## Next two prints is same but using different quotes
## Double quotes print example
print("Este es un ejemplo de impresión con comillas dobles.")
## Single quotes print example
print("Este es un ejemplo de impresión con comillas simples.")
