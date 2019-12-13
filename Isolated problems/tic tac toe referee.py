# given a tic-tac-toe game result as a list of strings (unicode), output "X", "O" or "D" depending on the outcome of
# the game

from typing import List

def checkio(game_result: List[str]) -> str:
    check_sets = game_result + ["".join(game_result[x][y] for x in range(3)) for y in range(3)] + ["".join(game_result[x][x] for x in range(3))] + ["".join(game_result[abs(x-2)][x] for x in range(3))]
    if "XXX" in check_sets:
        return "X"
    elif "OOO" in check_sets:
        return "O"
    else:
        return "D"

if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"