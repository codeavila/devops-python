#!/usr/bin/env python3
## 03 - Casting

# Casting to Integer
float_num = 9.7
int_num = int(float_num)
print("Número de punto flotante (float):", float_num, type(float_num))
print("Número entero (int):", int_num, type(int_num))

# Casting to Float
int_num2 = 5
float_num2 = float(int_num2)
print("Número entero (int):", int_num2, type(int_num2))
print("Número de punto flotante (float):", float_num2, type(float_num2))
## String to Float
str_num = "3.14"
float_num3 = float(str_num)
print("Número como cadena (str):", str_num, type(str_num))
print("Número de punto flotante (float):", float_num3, type(float_num3))

# Casting to String
num = 100
str_num = str(num)
print("Número entero (int):", num, type(num))
print("Número como cadena (str):", str_num, type(str_num))

# Casting to Boolean
zero_value = 0
bool_zero = bool(zero_value)
non_zero_value = 42
bool_non_zero = bool(non_zero_value)
print("Valor cero (0) como booleano:", bool_zero, type(bool_zero))
print("Valor no cero (42) como booleano:", bool_non_zero, type(bool_non_zero))

# Casting to List
tuple_data = (1, 2, 3)
list_data = list(tuple_data)
print("Tupla (tuple):", tuple_data, type(tuple_data))
print("Lista (list):", list_data, type(list_data))

# Casting to Tuple
list_data2 = [4, 5, 6]
tuple_data2 = tuple(list_data2)
print("Lista (list):", list_data2, type(list_data2))
print("Tupla (tuple):", tuple_data2, type(tuple_data2))

# Casting dictionary keys to a list
dict_data = {"a": 1, "b": 2, "c": 3}
keys_list = list(dict_data)
print("Diccionario (dict):", dict_data, type(dict_data))
print("Lista de claves (list):", keys_list, type(keys_list))
