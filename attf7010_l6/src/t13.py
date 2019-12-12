"""
------------------------------------------------------------------------
Task 13
Square-based Pyramid Geometry
------------------------------------------------------------------------
Author: Evan Attfield
ID:     180817010
Email:  attf7010@mylaurier.ca
Last Updated: Oct 30, 2018
------------------------------------------------------------------------
"""
from functions import square_pyramid

base = float(input('Length of base: '))
height = float(input('Perpendicular height of pyramid: '))

sh, a, v = square_pyramid(base, height)

print('')
print('Slant height of square pyramid: {:.2f}'.format(sh))
print('Area of square pyramid: {:.2f}'.format(a))
print('Volume of square pyramid: {:.2f}'.format(v))
