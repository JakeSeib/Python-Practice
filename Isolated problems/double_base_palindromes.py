# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

import math

def is_str_palindrome(str):
    """Given a string, return true if it is a palindrome, else return false"""
    # iterate over the first half of the characters in str
    # could have also used // for integer division instead of /
    for y in range(math.ceil(len(str) / 2)):
        if str[y] != str[-y - 1]:
            return False
    else:
        return True

def is_base_10_palindrome(num):
    """Given a number in base 10, returns true if that number is a palindrome in base 10, else return false"""

    num_str = str(num)
    return is_str_palindrome(num_str)

def is_base_2_palindrome(num):
    """Given a number in base 10, returns true if that number is a palindrome in base 2, else return false"""

    num_str = str(bin(num)[2:])
    return is_str_palindrome(num_str)

def find_double_base_palindromes(test_range):
    """Given an iterable of numbers to test, return the sum of all included numbers that are palindromic in base 10 and
    in base 2"""

    palindromes = []
    for x in test_range:
        if is_base_10_palindrome(x) and is_base_2_palindrome(x):
            palindromes.append(x)
    return sum(palindromes)

print(find_double_base_palindromes(range(1, 1000000)))
