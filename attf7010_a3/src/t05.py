"""
------------------------------------------------------------------------
Task 5
------------------------------------------------------------------------
Author: Evan Attfield
ID:     180817010
Email:  attf7010@mylaurier.ca
Last Updated: Sept 1, 2018
------------------------------------------------------------------------
"""

length = float(input('Length of call (minutes): '))
time = float(input('Hour of call (24 hour format): '))
BASE = 0.08
cost = length * BASE

if length > 30:
    cost *= 0.9
    if time >= 0 and time < 8:
        cost *= 0.5
        print('Total price of call: ${:,.2f}'.format(cost))
    elif time >= 18 and time < 24:
        cost *= 0.75
        print('Total price of call: ${:,.2f}'.format(cost))
    else:
        print('Total price of call: ${:,.2f}'.format(cost))
else:
    if time >= 0 and time < 8:
        cost *= 0.5
        print('Total price of call: ${:,.2f}'.format(cost))
    elif time >= 18 and time < 24:
        cost *= 0.75
        print('Total price of call: ${:,.2f}'.format(cost))
    else:
        print('Total price of call: ${:,.2f}'.format(cost))