"""
------------------------------------------------------------------------
Functions Depository
------------------------------------------------------------------------
Author: Evan Attfield, Colin Morenz
ID:     180817010, 180320150
Email:  attf7010@mylaurier.ca, more0150@mylaurier.ca
Last Updated: Nov 20, 2018
------------------------------------------------------------------------
"""

def get_customer_record(file_handle, n):
    """
    -------------------------------------------------------
    Find the n-th record in a comma-delimited sequential file.
    Records are numbered starting with 0.
    Use: result = get_customer_record(file_handle, n)
    -------------------------------------------------------
    Parameters:
        file_handle - file to search (file - open for reading)
        n - the number of the record to return (int > 0)
    Returns:
        result - a list of the fields of the n-th record if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    file_handle.seek(0)
    data = []
    count = 1
    # Read the first line of the file.
    line = file_handle.readline()

    while (line != "") and (count < n):
        # data.append(line.strip())
        line = file_handle.readline()
        count += 1
    if line != "":
        data.append(line.strip())

    return data

def number_stats(file_handle):
    """
    -------------------------------------------------------
    returns statistics on the numbers in a file.
    Use: smallest, largest, total, average = number_stats(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to search (file - open for reading)
    Returns:
        smallest - smallest number (int)
        largest - largest number (int)
        total - sum of all the numbers in the file (int)
        average - average of all the numbers (float)
    ------------------------------------------------------
    """
    file_handle.seek(0)

    line = file_handle.readline()
    value = int(line)
    min_val = int(line)
    max_val = int(line)
    total = int(line)
    counter = 1
    line = file_handle.readline()

    while (line != ""):
        # data.append(line.strip())
        # data.append(int(line))

        value = int(line)
        if value > max_val:
            max_val = value
        if value < min_val:
            min_val = value
        total = total + value
        counter += 1
        line = file_handle.readline()
    average = total / counter

    return (min_val, max_val, total, average)

def count_frequency_word(file_handle, word):
    """
    -------------------------------------------------------
    Counts the number of appearances of word in file_handle.
    Use: count = count_frequency_word(file_handle, word)
    -------------------------------------------------------
    Parameters:
        file_handle - file to search (file - open for reading)
        word - the word to search for it in file_handle
    Returns:
        count - the number of appearance of word in file_handle (int)
    ------------------------------------------------------
    """
    file_handle.seek(0)
    
    count = 0
    line = file_handle.readline()
    while line != "" :
        if word in line:
            count += 1
        line = file_handle.readline()
    
    return count

def find_shortest(file_handle):
    """
    -------------------------------------------------------
    Finds the first word with shortest length in file_handle.
    Use: word = find_longest(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to search (file - open for reading)
    Returns:
        word - the first word with the shortest length in file_handle (str)
    ------------------------------------------------------
    """
    file_handle.seek(0)
    
    line = file_handle.readline()
    word = line
    while line != "":
        if len(word) > len(line):
            word = line
        line = file_handle.readline()
    word = word.strip()
    return word

def file_copy(file_handle_1, file_handle_2):
    """
    -------------------------------------------------------
    Copies the contents of file_handle_1 to file_handle_2.
    Any contents of file_handle_2 are overwritten.
    Use: file_copy(file_handle_1, file_handle_2)
    -------------------------------------------------------
    Parameters:
        file_handle_1 - source file (file - open for reading)
        file_handle_2 - target file (file - open for writing)
    Returns:
        None
    ------------------------------------------------------
    """
    file_handle_1.seek(0)
    
    line = file_handle_1.readline()
    while line != "":
        print(line, file=file_handle_2, end="")
        #(what will be copied, file= the file to be copied to, the end of the copied stuff)
        line = file_handle_1.readline()
    
    