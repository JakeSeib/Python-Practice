# Originally was written to return the max length of substring without repeating characters; I now realize that I could
# have made a simple modification to that and returned the substring itself using len as the key for max. This would be
# much preferable to this version, had I realized originally that max could take len as a key.

def find_non_repeating(line, current_substring, substring_list, substring_num):
    if line[0] in current_substring:
        if len(line)>1:
            substring_list.append((current_substring, len(current_substring), substring_num))
            substring_num += 1
            return find_non_repeating(line[1:], current_substring[(current_substring.index(line[0])) + 1:] + line[0], substring_list, substring_num)
        else:
            substring_list.append((current_substring, len(current_substring), substring_num))
    else:
        substring = current_substring + line[0]
        if len(line)>1:
            return find_non_repeating(line[1:], substring, substring_list, substring_num)
        else:
            substring_list.append((substring, len(substring), substring_num))
    return substring_list

def non_repeat(line):
    """
        the longest substring without repeating chars
    """
    if line:
        return sorted(find_non_repeating(line, '', [], 0), key=lambda x: (-x[1], x[2]))[0][0]
    else:
        return ''

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    print('"Run" is good. How is "Check"?')