# Alex works at a clothing store. There is a large pile of socks that must be paired by color for sale. Given an array
# of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
#
# For example, there are n = 7 socks with colors ar = [1,2,1,2,1,3,2]. There is one pair of color 1 and one of color 2.
# There are three odd socks left, one of each color. The number of pairs is 2.
#
# Function Description
#
# Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching
# pairs of socks that are available.
#
# sockMerchant has the following parameter(s):
#
# n: the number of socks in the pile
# ar: the colors of each sock

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # can make dict to keep track of socks of each color, then look at length / 2 rounded down
    color_dict = {}
    pairs = 0
    for sock in ar:
        if sock in color_dict:
            color_dict[sock] += 1
        else:
            color_dict[sock] = 1
    print('color_dict', color_dict)
    for color in color_dict.keys():
        pairs += math.floor(color_dict[color]/2)
    return pairs

print(sockMerchant(3, [2, 3, 1]))
print(sockMerchant(7, [1,2,1,2,1,3,2]))