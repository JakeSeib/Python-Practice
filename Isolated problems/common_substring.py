# Given two strings, determine if they share a common substring. A substring may be as small as one character.
#
# For example, the words "a", "and", "art" share the common substring "a". The words "be" and "cat" do not share a substring.
#
# Function Description
#
# Complete the function twoStrings in the editor below. It should return a string, either YES or NO based on whether the strings share a common substring.
#
# twoStrings has the following parameter(s):
#
# s1, s2: two strings to analyze .

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    # minimum common substring is just 1 character
    # loop over s1, make a dict with keys of unique characters
    # go over s2, check for existence of each character in dict
    char_dict = {}
    for character in s1:
        if character not in char_dict:
            char_dict[character] = True
    if any(character in char_dict for character in s2):
        return 'YES'
    return 'NO'

print(twoStrings('bc?0', 'a'))