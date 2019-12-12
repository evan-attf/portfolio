"""
------------------------------------------------------------------------
Task 7
------------------------------------------------------------------------
Author: Evan Attfield
ID:     180817010
Email:  attf7010@mylaurier.ca
Last Updated: Oct 30, 2018
------------------------------------------------------------------------
"""
from functions import diameter, circumference, area

radius = float(input('Enter radius: '))
d = diameter(radius)
c = circumference(radius)
a = area(radius)

print('')
print('Diameter of circle: {}'.format(d))
print('Circumference of circle: {:.2f}'.format(c))
print('Area of circle: {:.2f}'.format(a))