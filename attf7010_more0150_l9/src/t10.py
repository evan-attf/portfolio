"""
------------------------------------------------------------------------
Records the frequency of appearance of a word in a file
Task 10
------------------------------------------------------------------------
Author: Evan Attfield
ID:     180817010
Email:  attf7010@mylaurier.ca
Last Updated: 
------------------------------------------------------------------------
"""
from functions import count_frequency_word

file_name = 'words.txt'
file_handle = open(file_name, 'r', encoding="utf-8")

print("file '{}' open for reading".format(file_name))
word = input('Word to count: ')

count = count_frequency_word(file_handle, word)
print("'{}' appears {} time(s)".format(word, count))

file_handle.close() 