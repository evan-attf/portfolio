"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Evan Attfield
ID:     180817010
Email:  attf7010@mylaurier.ca
Last Updated: 
------------------------------------------------------------------------
"""

PI = 3.14

d = float(input('Diameter of container base (cm): '))
h = float(input('Height of container (cm): '))
mat_cost = float(input('Cost of material ($/cm^2): '))
num_containers = int(input('Number of containers: '))

r = d / 2
area = PI*r**2 + 2*PI*h*r
one_cost = area * mat_cost
total_cost = one_cost * num_containers

print('The cost of one container is: ${:,.2f}'.format(one_cost))
print('The total cost of all containers is ${:,.2f}'.format(total_cost))