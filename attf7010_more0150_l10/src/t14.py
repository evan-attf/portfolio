"""
------------------------------------------------------------------------
Multiplies matrix by scalar
Task 14
------------------------------------------------------------------------
Author: Evan Attfield, Colin Morenz
ID:     180817010, 180320150
Email:  attf7010@mylaurier.ca, more0150@mylaurier.ca
Last Updated: 
------------------------------------------------------------------------
"""
from functions import generate_matrix_num, print_matrix_num, scalar_multiply

r = int(input('Number of rows: '))
c = int(input('Number of columns: '))
low = int(input('Low value: '))
high = int(input('High value: '))
value_type = 'int'
matrix = generate_matrix_num(r, c, low, high, value_type)

print('')
print('Matrix before scalar multiplication:')
print_matrix_num(matrix, value_type)

print('')
num = int(input('Enter number: '))

print('')
print('Matrix after scalar multiplication:')
scalar_multiply(matrix, num)