"""
------------------------------------------------------------------------
Task 1
------------------------------------------------------------------------
Author: Evan Attfield
ID:     180817010
Email:  attf7010@mylaurier.ca
Last Updated: Oct 1, 2018
------------------------------------------------------------------------
"""

num_balloons = int(input('Balloons collected: '))

if num_balloons < 1:
    print('Bonus points earned: 0')
elif num_balloons == 1:
    print('Bonus points earned: 10')
elif num_balloons == 2:
    print('Bonus points earned: 25')
else:
    print('Bonus points earned: 50')