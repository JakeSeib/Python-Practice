# The function should recognise if a subject line is stressful. A stressful subject line means that all letters are in
# uppercase, and/or ends by at least 3 exclamation marks, and/or contains at least one of the following “red” words:
# "help", "asap", "urgent". Any of those "red" words can be spelled in different ways - "HELP", "help", "HeLp",
# "H!E!L!P!", "H-E-L-P", even in a very loooong way "HHHEEEEEEEEELLP," they just can't have any other letters
# interspersed between them.

import re

def is_stressful(subj):
    stress_word_1 = re.compile("h+\W*e+\W*l+\W*p+",re.IGNORECASE)
    stress_word_2 = re.compile("a+\W*s+\W*a+\W*p+",re.IGNORECASE)
    stress_word_3 = re.compile("u+\W*r+\W*g+\W*e+\W*n+\W*t+",re.IGNORECASE)
    exclam_end = re.compile("!!!$")
    if subj == subj.upper():
        return True
    elif exclam_end.search(subj):
        return True
    elif stress_word_1.search(subj):
        return True
    elif stress_word_2.search(subj):
        return True
    elif stress_word_3.search(subj):
        return True
    else:
        return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"