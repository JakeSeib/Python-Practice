# Coding Practice
# This is a staircase of size n=3:
#   #
#  ##
# ###
# Its base and height are both equal to n. It is drawn using # symbols and spaces. The last line is not preceded by any
# spaces.
# Write a program that prints a staircase of size n. You can assume n is smaller than the width of your printing window
# and that your output is printed in a monospaced font.
#
# Thought experiment
# How could you cleanly modify your code to print fancy, tiled staircases, so that `staircase(5)` prints:
#     #
#    #%
#   #%#
#  #%#%
# #%#%#

def print_staircase(n):
    # staircase = ''
    # curr_step = 1
    # while curr_step <= n:
    #     staircase += ' ' * (n - curr_step) + '#' * curr_step + '\n'
    #     curr_step += 1
    # print(staircase)
    print('\n'.join([' ' * (n - curr_step) + '#%' * (curr_step // 2) + ('#' if curr_step % 2 > 0 else '') for curr_step in range(1, n + 1)]))

print_staircase(5)