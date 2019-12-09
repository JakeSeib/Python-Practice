# Find length of the longest substring that repeats more than once.

import re

def double_substring_helper(line, length):
    for x in range(0, len(line) - length):
        if len(re.findall(line[x:(x + length)], line)) > 1:
            return length
    return double_substring_helper(line, length - 1)

def double_substring(line):
    """
        length of the longest substring that non-overlapping repeats more than once.
    """
    initial_length = round(len(line)/2)
    if initial_length >= 1:
        return double_substring_helper(line, initial_length)
    else:
        return initial_length

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"