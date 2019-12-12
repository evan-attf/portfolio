"""
------------------------------------------------------------------------
Finds the smallest, largest, total, and average of a matrix
Task 7
------------------------------------------------------------------------
Author: Evan Attfield, Colin Morenz
ID:     180817010, 180320150
Email:  attf7010@mylaurier.ca, more0150@mylaurier.ca
Last Updated: 
------------------------------------------------------------------------
"""
from functions import print_matrix_num, generate_matrix_num, stats

r = int(input('Number of rows: '))
c = int(input('Number of columns: '))
low = int(input('Low value: '))
high = int(input('High value: '))

value_type = 'int'
matrix = generate_matrix_num(r, c, low, high, value_type)
print()
print_matrix_num(matrix, value_type)
print()
smallest, largest, total, average = stats(matrix)

print("""Smallest = {:}
Largest = {:}
Total = {:}
Average = {:.2f}""".format(smallest, largest, total, average))
