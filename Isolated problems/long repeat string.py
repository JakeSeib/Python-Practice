# Find the length of the longest substring that consists of the same letter.

import re

def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    letter_substring_lengths = []
    for letter in set(line):
        letter_repeat = re.compile(letter + '+')
        all_substrings = re.findall(letter_repeat,line)
        letter_substring_lengths.append(max([len(x) for x in all_substrings]))
    if letter_substring_lengths:
        return max(letter_substring_lengths)
    else:
        return 0

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"