"""
------------------------------------------------------------------------
Functions Depository
------------------------------------------------------------------------
Author: Evan Attfield, Colin Morenz
ID:     180817010, 180320150
Email:  attf7010@mylaurier.ca, more0150@mylaurier.ca
Last Updated: Nov 27, 2018
------------------------------------------------------------------------
"""
from random import randint
from random import uniform


def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """

    matrix = []

    if value_type == 'int':
        for _ in range(rows):
            subList = []
            for _ in range(cols):
                b = randint(low, high)
                subList.append(b)
            matrix.append(subList)
    elif value_type == 'float':
        for _ in range(rows):
            subList = []
            for _ in range(cols):
                a = uniform(low, high)
                subList.append(a)
            matrix.append(subList)
    return matrix


def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    print('  ', end='')
    for c in range(0, len(matrix[0]), 1):
        print('{:>7d}'.format(c), end='')
    print('')
    if value_type == 'int':
        for r in range(0, len(matrix), 1):
            print('{:>2d}'.format(r), end='')
            for c in range(0, len(matrix[r]), 1):
                print('{:>7d}'.format(matrix[r][c]), end='')
            print('')
    else:
        for r in range(0, len(matrix), 1):
            print('{:>2d}'.format(r), end='')
            for c in range(0, len(matrix[r]), 1):
                print('{:>7.2f}'.format(matrix[r][c]), end='')
            print('')
            
def stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
        Use: smallest, largest, total, average = stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """
    total = 0
    index_total = 0
    smallest = matrix[0][0]
    largest = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            index_total += 1
            if matrix[i][j] > largest:
                largest = matrix[i][j]
            elif matrix[i][j] < smallest:
                smallest = matrix[i][j]
            total = total + matrix[i][j]
    average = total / index_total
    return (smallest, largest, total, average)           

def find_less(matrix, n):
    """
    -------------------------------------------------------
    Finds the location [row, column] of the first value in matrix
    that is smaller than a target value, n. If there is no such
    number in matrix, it should return an empty list.
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
        n - the target value (float)
    Returns:
        loc - a list of the row and column location of
            the the first value smaller than n in values,
            an empty list otherwise (list of int)
    -------------------------------------------------------
    """
    loc = []
    
    for r in range(0, len(matrix), 1):
        for c in range(0, len(matrix), 1):
            if matrix[r][c] < n:
                loc.append(r)
                loc.append(c)
                return loc

def scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    ------------------------------------------------------
    """
    print('  ', end='')
    for c in range(0, len(matrix[0]), 1):
        print('{:>7d}'.format(c), end='')
    print('')
    
    for r in range(0, len(matrix), 1):
        print('{:>2d}'.format(r), end='')
        for c in range(0, len(matrix[r]), 1):
            print('{:>7d}'.format(matrix[r][c] * num), end='')
        print('')
    
            
    
    