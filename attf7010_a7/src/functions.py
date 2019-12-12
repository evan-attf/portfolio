"""
------------------------------------------------------------------------
Functions Depository
------------------------------------------------------------------------
Author: Evan Attfield
ID:     180817010
Email:  attf7010@mylaurier.ca
Last Updated: Nov 15, 2018
------------------------------------------------------------------------
"""

def my_isdigit(s):
    """
    -------------------------------------------------------
    Determines if all the characters is s are digits. An empty string
    has no digits.
    NOTE: must execute as the equivalent of the Python method s.isdigit()
    Use: digits = my_isdigit(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        digits - True if all of s is digits, False otherwise (boolean)
    -------------------------------------------------------
    """
    l = 0 
    
    for i in range(0, len(s), 1):
        if s[i] in '1234567890':
            l += 1
            
    if  l == len(s):
        return True
    else:
        return False

def my_isalpha(s):
    """
    -------------------------------------------------------
    Determines if all the characters is s are alphabetic characters.
    An empty string has no letters.
    NOTE: must execute as the equivalent of the Python method s.isalpha()
    Use: alpha = my_isalpha(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        alpha - True if all of s is letters of the alphabet,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    l = 0
    
    for i in range(0, len(s), 1):
        if s[i] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            l += 1
            
    if  l == len(s):
        return True
    else:
        return False

def my_find(s, r):
    """
    -------------------------------------------------------
    Returns the index of the string r in the string s.
    NOTE: must execute as the equivalent of the Python method s.find(r)
    Use: i = my_find(s, r)
    -------------------------------------------------------
    Parameters:
        s - a string to search (str)
        r - a string to search for (str)
    Returns:
        i - the index of the start of r in s, -1 if r is not in s (int)
    -------------------------------------------------------
    """
    if r in s:
        i = 0
        while r in s[i:]:
            i += 1
        i -= 1
    else:
        i = -1
    return i

def common_ending(s1, s2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: common = common_ending(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - first string for ending comparison (str)
        s2 - second string for ending comparison (str)
    Returns:
        common - the longest common ending of s1 and s2 (str)
    -------------------------------------------------------
    """
    i = 1
    if s1 == s2:
        common = s1
    elif s1[(len(s1) - 1):] != s2[(len(s2) - 1):]:
        common = ''
    else:
        while s1[(len(s1) - i):] == s2[(len(s2) - i):]:
            i += 1
            common = s1[(len(s1) - i + 1):] 
    return common         
    
def is_valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: valid = is_valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    dash = 0
    for_test = True
    for i in range(0, len(isbn), 1):
        if isbn [i] not in '1234567890-': #only digits and dashes
            #print('only digits and dashes')
            for_test = False
        elif isbn[i] == '-':
            dash += 1
            
            if isbn[i - 1] == '-': #adjacent dashes
                #print('adjacent dashes')
                for_test = False
    
    if len(isbn) != 17: #length check
        #print('length check')
        valid = False
    elif dash != 4: #dash check
        #print('dash check')
        valid = False
    elif isbn[:3] != '978' and isbn[:3] != '979': #prefix check
        #print('prefix check')
        valid = False
    elif isbn[len(isbn) - 2] != '-' and isbn[len(isbn) - 1] not in '1234567890': #last group is a single digit
        #print('last group is single digit')
        valid = False
    elif for_test != True: #checks if for_test is false from the for loop
        valid = False 
    else:
        valid = True
    return valid

def number_convert(number):
    """
    -------------------------------------------------------
    Converts a phone number character string to a string of digits.
    A telephone keypad has the following digit/letter combinations:
        2 : ABC
        3 : DEF
        4 : GHI
        5 : JKL
        6 : MNO
        7 : PRS
        8 : TUV
        9 : WXY
    ('Q' and 'Z' are not represented.) Q, Z, and non-letters are
    left unchanged.
    Use: digits = number_convert(number)
    -------------------------------------------------------
    Parameters:
        number - a phone number string (str)
    Returns:
        digits - the numeric version of number based upon a
            telephone keypad (str)
    -------------------------------------------------------
    """
    digits = number
    for i in range(0, len(digits), 1):
        if digits[i] in 'ABC':
            digits = digits[:i] + '2' + digits[i + 1:]
        elif digits[i] in 'DEF':
            digits = digits[:i] + '3' + digits[i + 1:]
        elif digits[i] in 'GHI':
            digits = digits[:i] + '4' + digits[i + 1:]
        elif digits[i] in 'JKL':
            digits = digits[:i] + '5' + digits[i + 1:]
        elif digits[i] in 'MNO':
            digits = digits[:i] + '6' + digits[i + 1:]
        elif digits[i] in 'PRS':
            digits = digits[:i] + '7' + digits[i + 1:]
        elif digits[i] in 'TUV':
            digits = digits[:i] + '8' + digits[i + 1:]
        elif digits[i] in 'WXY':
            digits = digits[:i] + '9' + digits[i + 1:]
    return digits
            
def pluralize(s):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if s ends with 's', 'sh', or 'ch', add 'es'
        - if s ends with 'y' but not 'ay' or 'oy', add 'ies'
        - otherwise add 's'
    Use: plural = pluralize(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        plural - a plural version of s (str)
    -------------------------------------------------------
    """
    if s[(len(s) - 1):] == 's' or s[(len(s) - 2):] in 'shch':
        plural = s + 'es'
    elif s[(len(s) - 1):] == 'y' and s[(len(s) - 2):] not in 'ayoy':
        plural = s[:(len(s) - 1)] + 'ies'
    else:
        plural = s + 's'
    return plural