# given two strings with words separated by commas, find all of the words that appear in both strings. The words are not
# repeated in the same string.

# result must is string of words separated by commas in alphabetic order.

def checkio(first, second):
    common_words = sorted(set(first.split(",")).intersection(set(second.split(","))))
    common_words_string = ",".join(common_words)
    return common_words_string

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
