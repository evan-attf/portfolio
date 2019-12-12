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
from functions import get_customer_record
# Imports
file_handle = "customers.txt"
print("Find record n")
n = int(input("Enter a record number: "))


file_name = "customers.txt"
customerFile = open(file_name, "r", encoding="utf-8")
customerData = get_customer_record(customerFile, n)
customerFile.close()
print(customerData)