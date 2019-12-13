# game board laid out in eight rows (called ranks and denoted with numbers 1 to 8) and eight columns (called files and
# denoted with letters a to h)

# a pawn may capture an opponent's piece on a square diagonally in front of it on an adjacent file, by moving to that
# square. For white pawns the front squares are squares with greater row number than the square they currently occupy

# given a set of coordinates for white pawns, return how many pawns are 'safe' (i.e. on a space able to be captured by
# other white pawns)

# 0 < pawns ≤ 8

import string

def safe_pawns(pawns: set) -> int:
    coord_tuples = [(item[0], int(item[1])) for item in pawns]
    safe_count = 0
    for tuple in coord_tuples:
        if (string.ascii_lowercase[string.ascii_lowercase.index(tuple[0]) + 1] + str(tuple[1] - 1) in pawns) or (string.ascii_lowercase[string.ascii_lowercase.index(tuple[0]) - 1] + str(tuple[1] - 1) in pawns):
            safe_count += 1
    print(safe_count)
    return safe_count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1