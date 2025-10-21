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

# Insert value at specific index
fruits.insert(1, "banana")
print(fruits)  # Output: ['apple', 'banana', 'blueberry', 'cherry', 'date']

# Removing elements from the list
fruits.remove("cherry")
print(fruits)  # Output: ['apple', 'banana', 'blueberry', 'date']

# List length
print(len(fruits))  # Output: 4

# Extend a list with another list => this method adds each elemento at the end of the list
more_fruits = ["elderberry", "fig", "grape"]
fruits.extend(more_fruits)
print(
    fruits
)  # Output: ['apple', 'banana', 'blueberry', 'date', 'elderberry', 'fig', 'grape']

# Delete a Index from a list using pop()
fruits.pop(2)
print(fruits)  # Output: ['apple', 'banana', 'date', 'elderberry', 'fig', 'grape']

# Delete a Index from a list using del => best practice is when you need to remove a range of elements
del fruits[3]
print(fruits)  # Output: ['apple', 'banana', 'date', 'fig', 'grape']
## Range delete example
del fruits[1:3]
print(fruits)  # Output: ['apple', 'fig', 'grape']

# Delete all elements from a list
fruits.clear()
print(fruits)  # Output: []

# Order list elements SORT => modifies the original list
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 5, 6, 9]
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 6, 5, 5, 2, 1]
## SORT without modifying the original list using sorted()
unsorted_numbers = [3, 8, 4, 2, 7]
sorted_numbers = sorted(unsorted_numbers)
print(unsorted_numbers)  # Output: [3, 8, 4, 2, 7]
print(sorted_numbers)  # Output: [2, 3, 4, 7, 8]

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
List slicing: list[:end]
List slicing: list[start:]
Add element: list.append(element)
Remove element: list.remove(element)
Get length: len(list)
"""
# Examples Cheatsheet
sample_list = [10, 20, 30, 40, 50]
print(sample_list[-1])  # Output: 50
print(sample_list[1:4])  # Output: [20, 30, 40]
print(sample_list[:3])  # Output: [10, 20, 30]
print(sample_list[2:])  # Output: [30, 40, 50]
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

"""
Copy a list before modifying it to avoid changing the original list.
"""
original_list = [1, 2, 3]
copied_list = original_list.copy()
copied_list.append(4)
print("Original List:", original_list)  # Output: [1, 2, 3]
print("Copied List:", copied_list)  # Output: [1, 2,3, 4]

# Second way to copy a list using slicing
sliced_list = original_list[:]
sliced_list.append(5)
print("Original List:", original_list)  # Output: [1, 2, 3]
print("Sliced List:", sliced_list)  # Output: [1, 2, 3, 5]

"""
List Slicing with Step:
original_list = [start:end:step]
start => starting index (inclusive)
end => ending index (exclusive)
step => step size (optional, default is 1) => skips elements based on step size
Example: original_list[0:5:2] => gets elements from index 0 to 4, skipping every second element
"""
# Example of slicing with step
example_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sliced_with_step = example_list[0:10:2]
print(sliced_with_step)  # Output: [0, 2, 4, 6, 8]


"""
Cheat reverse a list using slicing:
reversed_list = original_list[::-1]
"""
# Example of reversing a list
numbers = [1, 2, 3, 4, 5]
reversed_numbers = numbers[::-1]
print(reversed_numbers)  # Output: [5, 4, 3, 2, 1]


"""
Contact List Elements:
"""
# Example of concatenating lists
numbers = [1, 2, 3]
second_numbers = [4, 5, 6]
combined = numbers + second_numbers
print(combined)  # Output: [1, 2, 3, 4, 5, 6]

# Short way using +=
numbers += second_numbers
print(numbers)  # Output: [1, 2, 3, 4, 5, 6]
