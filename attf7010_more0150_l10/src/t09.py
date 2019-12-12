"""
------------------------------------------------------------------------
Finds the location [row, column] of the first value in matrix
    that is smaller than a target value, n. If there is no such
    number in matrix, it should return an empty list.
Task 9
------------------------------------------------------------------------
Author: Evan Attfield, Colin Morenz
ID:     180817010, 180320150
Email:  attf7010@mylaurier.ca, more0150@mylaurier.ca
Last Updated: Nov 27, 2018
------------------------------------------------------------------------
"""
from functions import generate_matrix_num, print_matrix_num, find_less

r = int(input('Number of rows: '))
c = int(input('Number of columns: '))
low = int(input('Low value: '))
high = int(input('High value: '))
value_type = 'int'
matrix = generate_matrix_num(r, c, low, high, value_type)

print('')
print_matrix_num(matrix, value_type)

print('')
n = int(input('Number to find: ')) #This was put here upon request from TA
loc = find_less(matrix, n)

print('')
print('Position:', loc)
if loc != None:
    print('Value:', matrix[loc[0]][loc[1]])
else:
    print('Value: N/A')