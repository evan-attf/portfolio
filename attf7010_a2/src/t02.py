"""
------------------------------------------------------------------------
Task 2
------------------------------------------------------------------------
Author: Evan Attfield
ID:     180817010
Email:  attf7010@mylaurier.ca
Last Updated: Sept 26, 2018
------------------------------------------------------------------------
"""

STUDENT_DISCOUT = 80/100

cost = float(input('Cost of movie: '))
cost *= STUDENT_DISCOUT
print('The cost of the movie for a student is ${:,.2f}.'.format(cost))
