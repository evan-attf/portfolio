"""
------------------------------------------------------------------------
Finds the shortest word in a file
Task 12
------------------------------------------------------------------------
Author: Evan Attfield
ID:     180817010
Email:  attf7010@mylaurier.ca
Last Updated: Nov 20, 2018
------------------------------------------------------------------------
"""
from functions import find_shortest

file_name = 'words.txt'
file_handle = open(file_name, 'r', encoding="utf-8")

print("file '{}' open for reading".format(file_name))
word = find_shortest(file_handle)

print("'{}' is the first shortest word".format(word))