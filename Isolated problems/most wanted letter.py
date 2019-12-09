# Find the most frequent letter in the text. Return the letter in lower case.
# While checking for the most wanted letter, casing does not matter. Does not consider punctuation symbols, digits and
# whitespaces.
# Ties broken by alphabetical order.

from string import ascii_lowercase

def checkio(text: str) -> str:
    mwl, mwl_count = "", 0
    for letter in ascii_lowercase[::-1]:
        letter_count = text.lower().count(letter)
        if letter_count >= mwl_count:
            mwl_count = letter_count
            mwl = letter
    return mwl

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")