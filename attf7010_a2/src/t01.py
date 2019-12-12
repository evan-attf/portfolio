"""
------------------------------------------------------------------------
Task 1
------------------------------------------------------------------------
Author: Evan Attfield
ID:     180817010
Email:  attf7010@mylaurier.ca
Last Updated: Sept 24, 2018
------------------------------------------------------------------------
"""

sales = float(input('Enter projected annual sales: $'))
PROFIT_PERCENT = 18/100 #percent of sales as profit
profit = sales * PROFIT_PERCENT

print('The projected profit on sales of ${:,.2f} is ${:,.2f}.'.format(sales, profit))
