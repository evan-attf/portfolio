"""
------------------------------------------------------------------------
Generates a matrix
Task 1
------------------------------------------------------------------------
Author: Evan Attfield, Colin Morenz
ID:     180817010, 180320150
Email:  attf7010@mylaurier.ca, more0150@mylaurier.ca
Last Updated: Nov 27, 2018
------------------------------------------------------------------------
"""
from functions import generate_matrix_num

rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))
low = float(input("Low value: "))
high = float(input("High value: "))
value_type = input("Type of values: ")


matrix = generate_matrix_num(rows, cols, low, high, value_type)

print('')
print(matrix)