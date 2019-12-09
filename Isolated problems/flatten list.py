# Given a nested list with integers, output the one-dimensional list with integers. Solution should be shorter than 140
# characters (with whitespaces).

from collections.abc import Iterable

def flat_list (array):
    if isinstance(array, Iterable) and not isinstance(array, (str, bytes)):
        return [a for i in array for a in flat_list(i)]
    else:
        return [array]

if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, ["string", 6, [6], 6, 6, 6], 7]]) == [2, 4, "string", 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"