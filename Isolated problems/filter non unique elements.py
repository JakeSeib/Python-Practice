# Given a non-empty list of integers, return a list consisting of only the non-unique elements in this list, i.e. remove
# all unique elements (elements which are contained in a given list only once) without changing the order of the list.

def checkio(data: list) -> list:
    non_uniques = data[:]
    for i in set(data):
        if data.count(i) == 1:
            non_uniques.remove(i)
    return non_uniques

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
