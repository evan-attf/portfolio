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
# Imports
from functions import number_stats

number_data = "numbers.txt"
file_handle = open(number_data, "r", encoding="utf-8")
min_val, max_val, total_val, average = number_stats(file_handle)
file_handle.close()
print("""Smallest: {}
Largest: {}
Total: {:.2f}
Average: {:.2f}""".format(min_val, max_val, total_val, average))
