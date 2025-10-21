#!/usr/bin/env python3

## 02 - List Operations and User Input

# Example list
fruits = ["apple", "banana", "cherry"]

# Accessing list elements
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry

# Modifying list elements
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# Adding elements to the list
fruits.append("date")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date']

# Removing elements from the list
fruits.remove("cherry")
print(fruits)  # Output: ['apple', 'blueberry', 'date']

# List length
print(len(fruits))  # Output: 3

# User input
new_fruit = input("Enter a new fruit: ")
fruits.append(new_fruit)
print(fruits)

# List mixing types
mixed_list = [1, "two", 3.0, True]
print(mixed_list)  # Output: [1, 'two', 3.0, True]
# Accessing mixed list elements
for item in mixed_list:
    print(f"Item: {item}, Type: {type(item)}")


# List of lists or matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0])  # Output: [1, 2, 3]
print(matrix[1][2])  # Output: 6
# Modifying elements in a list of lists
matrix[2][1] = 88
print(matrix)  # Output: [[1, 2, 3], [4, 5, 6], [7, 88, 9]]


"""
Cheatsheet of List Operations:
List last element: list[-1]
List slicing: list[start:end]
Add element: list.append(element)
Remove element: list.remove(element)
Get length: len(list)
"""
# Examples Cheatsheet
sample_list = [10, 20, 30, 40, 50]
print(sample_list[-1])  # Output: 50
print(sample_list[1:4])  # Output: [20, 30, 40]
sample_list.append(60)
print(sample_list)  # Output: [10, 20, 30, 40, 50, 60]
sample_list.remove(30)
print(sample_list)  # Output: [10, 20, 40, 50, 60]
print(len(sample_list))  # Output: 5

# Cheatsheet matrix examples
sample_matrix = [[1, 2], [3, 4], [5, 6]]
print(sample_matrix[-1])  # Output: [5, 6]
print(sample_matrix[1][0])  # Output: 3
sample_matrix.append([7, 8])
print(sample_matrix)  # Output: [[1, 2], [3, 4], [5, 6], [7, 8]]
sample_matrix.remove([3, 4])
print(sample_matrix)  # Output: [[1, 2], [5, 6], [7, 8]]
print(len(sample_matrix))  # Output: 3
