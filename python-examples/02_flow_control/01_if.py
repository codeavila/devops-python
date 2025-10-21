#!/usr/bin/env python3

## 01 - If Statements

"""
This script demonstrates the use of if, elif, and else statements in Python.
It includes examples of comparison operators, logical operators, and nested conditions.
"""

# Example variables
age = 20
is_student = True
# If statement
if age < 18:
    print("Eres menor de edad.")
elif 18 <= age < 65:
    print("Eres un adulto.")
    # Nested if statement
    if is_student:
        print("Eres un estudiante adulto.")
    else:
        print("No eres un estudiante.")

"""
else statement is only executed if none of the above conditions are true.
its optional and can be omitted if not needed.
"""


"""
Logic operators can be used to combine multiple conditions.
and =>  all conditions must be true
or => at least one condition must be true
not => negates a condition
"""
# Example with logical operators
if age < 18 or is_student:
    print("Tienes descuento especial.")

if not is_student:
    print("No tienes descuento de estudiante.")

# Example with multiple conditions
if age >= 18 and age < 65 and not is_student:
    print("Eres un adulto no estudiante.")


"""
Table of Comparison Logical Operators:
| Operator | Description               | Example          |
|----------|---------------------------|------------------|
| ==       | Equal to                  | age == 18        |
| !=       | Not equal to              | age != 18        |
| >        | Greater than              | age > 18         |
| <        | Less than                 | age < 18         |
| >=       | Greater than or equal to   | age >= 18       |
| <=       | Less than or equal to      | age <= 18       |
| and      | Logical AND               | age > 18 and is_student |
| or       | Logical OR                | age < 18 or is_student  |
| not      | Logical NOT               | not is_student   |
"""
