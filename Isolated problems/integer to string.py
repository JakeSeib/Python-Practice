# Given A number as an integer, output the string representation of the number

# 0 < number < 1000

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def str_num_under_100(number):
    """Given an integer < 100, return the string representation of that integer"""
    num_string = ""
    if 0 < number < 10:
        num_string = FIRST_TEN[number - 1]
    elif 10 <= number < 20:
        num_string = SECOND_TEN[number - 10]
    elif 20 <= number < 100:
        digit_1 = OTHER_TENS[int(str(number)[0]) - 2]
        if int(str(number)[1]) > 0:
            digit_2 = " " + FIRST_TEN[int(str(number)[1]) - 1]
        else:
            digit_2 = ""
        num_string = digit_1 + digit_2
    return num_string

def checkio(number):
    if number < 100:
        return str_num_under_100(number)
    else:
        digit_1 = FIRST_TEN[int(str(number)[0]) - 1] + " " + HUNDRED
        digits_2_3 = str_num_under_100(int(str(number)[1:3]))
        if digits_2_3:
            num_string = digit_1 + " " + digits_2_3
        else:
            num_string = digit_1 + digits_2_3
    return num_string


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"