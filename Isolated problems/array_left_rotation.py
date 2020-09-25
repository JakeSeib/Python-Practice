# A left rotation operation on an array shifts each of the array's elements 1 unit to the left. For example, if 2 left
# rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2].
#
# Given an array a of n integers and a number, d, perform d left rotations on the array. Return the updated array to be
# printed as a single line of space-separated integers.
#
# Function Description
#
# Complete the function rotLeft in the editor below. It should return the resulting array of integers.
#
# rotLeft has the following parameter(s):
#
# - An array of integers a.
# - An integer d, the number of rotations.

# Complete the rotLeft function below.

import math

def rotLeft(a, d):
    # calculate the overall shift of the array
    # full rotations can be ignored
    net_shift = d - math.floor(d/len(a))*len(a)
    # slice off an appropriately-sized section from the beginning and add it to the end
    return a[net_shift:len(a)] + a[0:net_shift]

print(rotLeft([1,2,3,4,5], 8))