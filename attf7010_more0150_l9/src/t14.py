"""
------------------------------------------------------------------------
Copies the contents of one file to another
Task 14
------------------------------------------------------------------------
Author: Evan Attfield
ID:     180817010
Email:  attf7010@mylaurier.ca
Last Updated: Nov 20, 2018
------------------------------------------------------------------------
"""
from functions import file_copy

file_name_1 = 'words.txt'
file_handle_1 = open(file_name_1, 'r', encoding="utf-8")
file_name_2 = 'new_words.txt'
file_handle_2 = open(file_name_2, 'w', encoding="utf-8")

print("Copying '{}' to '{}'".format(file_name_1, file_name_2))
file_copy(file_handle_1, file_handle_2)

file_handle_1.close() 
file_handle_2.close() 