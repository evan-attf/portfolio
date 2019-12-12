"""
------------------------------------------------------------------------
Functions Depository
------------------------------------------------------------------------
Author: Evan Attfield
ID:     180817010
Email:  attf7010@mylaurier.ca
Last Updated: Oct 30, 2018
------------------------------------------------------------------------
"""

def sum_partial_harmonic(n):
    """
    -------------------------------------------------------
    Sums and returns the total of a partial harmonic series.
    This series is the sum of all terms 1/i, where i ranges
    from 1 to n (inclusive)
    i.e. 1 + 1/2 + 1/3 + ... + 1/n
    Use: total = sum_partial_harmonic(n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int > 0)
    Returns:
        total - sum of partial harmonic series from 1 to n (int)
    ------------------------------------------------------
    """
    harmonic_sum = 0
    for i in range(1, n+1, 1):
        harmonic_sum += (1/i)
    return harmonic_sum

def draw_triangle(height, char):
    """
    -------------------------------------------------------
    Prints a triangle of height characters using
    the char character.
    Use: draw_triangle(height, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    
    for j in range (1, height+1, 1):
        char_num = 1 + (2*(j-1))
        space_num = ((height*2 - 1) - char_num) // 2
        for _ in range(space_num):
            print(' ', end='')
        for _ in range(char_num):
            print('{}'.format(char), end='')
        for _ in range(space_num):
            print(' ', end='')
        print('')
             
def diameter(radius):
    """
    -------------------------------------------------------
    Calculates and returns diameter of a circle.
    Use: d = diameter(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        d - diameter of a circle (float)
    ------------------------------------------------------
    """
    
    return (radius*2)
    
def circumference(radius):
    """
    -------------------------------------------------------
    Calculates and returns circumference of a circle.
    Use: c = circumference(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        c - circumference of a circle (float)
    ------------------------------------------------------
    """
    PI = 3.14
    
    return (2*PI*radius)
    
def area(radius):
    """
    -------------------------------------------------------
    Calculates and returns area of a circle.
    Use: a = area(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        a - area of a circle (float)
    ------------------------------------------------------
    """
    PI = 3.14
    
    return (PI*(radius**2))
    
def is_leap(year):
    """
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
            False otherwise (bool)
    ------------------------------------------------------
    """
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def square_pyramid(base, height):
    """
    -------------------------------------------------------
    Calculates and returns the slant height, area, and
    volume of a square pyramid given the base and perpendicular
    height.
    Use: sh, a, v = square_pyramid(base, height)
    -------------------------------------------------------
    Parameters:
        base - length of the base of the pyramid (float > 0)
        height - perpendicular height of the pyramid (float > 0)
    Returns:
        sh - slant height of the square pyramid (float)
        a - area of the square pyramid (float)
        v - volume of the square pyramid (float)
    ------------------------------------------------------
    """
    import math
    
    sh = math.sqrt((base/2)**2 + height**2)
    a = base**2 + 2*base*(math.sqrt((base**2 / 4) + height**2))
    v = base**2 * height/3
    
    return (sh, a, v)
            
                