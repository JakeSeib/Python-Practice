# return a roman numeral using the specified integer value ranging from 1 to 3999

def digit_to_roman_numeral(number):
    """Given an integer from 1 to 3999, return the corresponding Roman numeral as a string.

    Letter M can appear as many times as possible.
    Letters D, L, and V should not appear more than once.
    Letters C, X, and I should not appear more than 3 times, and their placement depends on the specific number, i.e.
    4 is written as: IV, but
    7 is written as: VII"""

    return_val = ''
    curr_num = number
    roman_numerals = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    roman_numeral_vals = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    # check if M's are needed
    if curr_num >= 1000:
        num_m = curr_num // 1000
        curr_num = curr_num - (1000 * num_m)
        return_val += 'M' * num_m
    # digits of 9 have specific representation
    if curr_num >= 900:
        curr_num -= 900
        return_val += 'CM'
    # check if D's are needed
    if curr_num >= 500:
        curr_num -= 500
        return_val += 'D'
    # digits of 4 have specific representation
    elif curr_num >= 400:
        curr_num -= 400
        return_val += 'CD'
    # check if C's are needed
    if curr_num >= 100:
        num_c = curr_num // 100
        curr_num = curr_num - (100 * num_c)
        return_val += 'C' * num_c
    # digits of 9 have specific representation
    if curr_num >= 90:
        curr_num -= 90
        return_val += 'XC'
    # check if L's are needed
    if curr_num >= 50:
        curr_num -= 50
        return_val += 'L'
    # digits of 4 have specific representation
    elif curr_num >= 40:
        curr_num -= 40
        return_val += 'XL'
    # check if X's are needed
    if curr_num >= 10:
        num_x = curr_num // 10
        curr_num = curr_num - (10 * num_x)
        return_val += 'X' * num_x
    # digits of 9 have specific representation
    if curr_num >= 9:
        curr_num -= 9
        return_val += 'IX'
    # check if V's are needed
    if curr_num >= 5:
        curr_num -= 5
        return_val += 'V'
    # digits of 4 have specific representation
    elif curr_num >= 4:
        curr_num -= 4
        return_val += 'IV'
    num_i = curr_num
    return_val += 'I' * num_i

    return return_val

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_to_roman_numeral(6) == 'VI', '6'
    assert digit_to_roman_numeral(76) == 'LXXVI', '76'
    assert digit_to_roman_numeral(499) == 'CDXCIX', '499'
    assert digit_to_roman_numeral(3888) == 'MMMDCCCLXXXVIII', '3888'

print(digit_to_roman_numeral(3999))
#MMMDCCCCLXXXXVIIII
#"MMMCMXCIX"

