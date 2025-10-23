#!/usr/bin/env python3

## 04 - Variables
"""
Python dont need explicit declaration of variables.
A variable is created the moment you first assign a value to it.
"""
# Variable assignment
x = 10
y = 5.5
name = "CodeCraftAvila"
is_student = True


"""
Python is dynamically typed, so you can reassign variables to different data types without any issues.
You dont need to declare the type of variable explicitly.
"""
# Variable can reassign to different data types
x = "Now I'm a string"
x = 42.0


"""
Not recommended declare multiple variables in one line, but possible.
"""
# Multiple variable assignment
a, b, c = 1, 2.5, "Hello"

# Conventionally name variables using lowercase letters and underscores
first_name = "Ana"
last_name = "Gomez"

# Constant variables (you can simulate but python does not have true constants)
# Its just for visual indication that this variable should not be changed
PI = 3.14159


"""
Dont use next names
=> Start with number => 1st_variable
=> my-variable 
=> Use special characters
=> Use Python reserved words like: print, if, else, for, while, etc.
"""


"""
Best practices
You can assign types to variables, but its not required
 => The type hints is a annotation that helps with code readability and tooling support. <=
"""
age: int = 30
height: float = 5.9
is_active: bool = True
