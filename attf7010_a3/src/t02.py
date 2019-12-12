"""
------------------------------------------------------------------------
Task 2
------------------------------------------------------------------------
Author: Evan Attfield
ID:     180817010
Email:  attf7010@mylaurier.ca
Last Updated: Oct 1, 2018
------------------------------------------------------------------------
"""

watts = int(input('Lightbulb wattage (w): '))

if watts == 15:
    print('Brightness: 125 lumens')
elif watts == 25:
    print('Brightness: 215 lumens')
elif watts == 40:
    print('Brightness: 500 lumens')
elif watts == 60:
    print('Brightness: 880 lumens')
elif watts == 75:
    print('Brightness: 1000 lumens')
elif watts == 100:
    print('Brightness: 1675 lumens')
else:
    print('Invalid wattage')