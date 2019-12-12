"""
------------------------------------------------------------------------
Task 4
------------------------------------------------------------------------
Author: Evan Attfield
ID:     180817010
Email:  attf7010@mylaurier.ca
Last Updated: Oct 1, 2018
------------------------------------------------------------------------
"""

c1 = input('Enter first colour: ')
c2 = input('Enter second colour: ')

if c1 == 'red':
    if c2 == 'blue':
        print('Secondary colour is purple')
    elif c2 == 'yellow':
        print('Secondary colour is orange')
    else:
        print('No secondary colour')
elif c1 == 'blue':
    if c2 == 'red':
        print('Secondary colour is purple')
    elif c2 == 'yellow':
        print('Secondary colour is green')
    else:
        print('No secondary colour')
elif c1 == 'yellow':
    if c2 == 'red':
        print('Secondary colour is orange')
    elif c2 == 'blue':
        print('Secondary colour is green')
    else:
        print('No secondary colour')
else:
    print('No secondary colour')
        