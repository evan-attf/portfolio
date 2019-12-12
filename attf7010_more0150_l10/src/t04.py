"""
------------------------------------------------------------------------
Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
Task 4
------------------------------------------------------------------------
Author: Evan Attfield, Colin Morenz
ID:     180817010, 180320150
Email:  attf7010@mylaurier.ca, more0150@mylaurier.ca
Last Updated: Nov 27, 2018
------------------------------------------------------------------------
"""
from functions import print_matrix_num, generate_matrix_num

r = int(input('Number of rows: '))
c = int(input('Number of columns: '))
low = int(input('Low value: '))
high = int(input('High value: '))
value_type = input('Type of values: ')
matrix = generate_matrix_num(r, c, low, high, value_type)

print('')
print_matrix_num(matrix, value_type)

