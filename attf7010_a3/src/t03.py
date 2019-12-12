"""
------------------------------------------------------------------------
Task 3
------------------------------------------------------------------------
Author: Evan Attfield
ID:     180817010
Email:  attf7010@mylaurier.ca
Last Updated: Oct 1, 2018
------------------------------------------------------------------------
"""

p1 = input('Enter Player 1 choice (R, P, or S): ')
p2 = input('Enter Player 2 choice (R, P, or S): ')

if p1 == 'R':
    if p2 == 'R':
        print('A tie!')
    elif p2 == 'P':
        print('Paper beats rock! Player 2 wins.')
    else:
        print('Rock beats scissors! Player 1 wins.')
elif p1 == 'P':
    if p2 == 'R':
        print('Paper beats rock! Player 1 wins.')
    elif p2 == 'P':
        print('A tie!')
    else:
        print('Scissors beats paper! Player 2 wins.')
else:
    if p2 == 'R':
        print('Rock beats scissors! Player 2 wins.')
    elif p2 == 'P':
        print('Scissors beat paper! Player 1 wins.')
    else:
        print('A tie!')