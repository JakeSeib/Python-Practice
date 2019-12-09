# Translate bird language. The bird converts words by two rules:
# - after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
# - after each vowel letter the bird appends two of the same letter (a ⇒ aaa);
# All words are lowercase, no punctuation.

VOWELS = "aeiouy"

def fix_vowels(phrase):
    for x in VOWELS:
        phrase = phrase.replace(3*x,x)
    return phrase

def translate(phrase):
    return translate_helper(fix_vowels(phrase))

def translate_helper(phrase):
    if len(phrase) <= 1:
        return phrase
    else:
        current_letter = phrase[0]
        if current_letter in (" " + VOWELS):
            return current_letter + translate_helper(phrase[1:])
        else:
            return current_letter + translate_helper(phrase[2:])

if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"