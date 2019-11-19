#My solution for Checkio's "Bird Language" problem in "Home." Left here as an example of a recursive function

VOWELS = "aeiouy"

def translate(phrase):
    return translate_helper(fix_vowels(phrase))

def fix_vowels(phrase):
    for x in VOWELS:
        phrase = phrase.replace(3*x,x)
    return phrase

def translate_helper(phrase):
    if len(phrase) <= 1:
        return phrase
    else:
        current_letter = phrase[0]
        if current_letter in (" " + VOWELS):
            return current_letter + translate_helper(phrase[1:])
        else:
            return current_letter + translate_helper(phrase[2:])

print(translate("hieeelalaooo") == "hello")
print(translate("hoooowe yyyooouuu duoooiiine") == "how you doin")
print(translate("aaa bo cy da eee fe") == "a b c d e f")
print(translate("sooooso aaaaaaaaa") == "sos aaa")