# Compute how many different ways a given integer can be expressed as a sum of consecutive positive integers (i.e. 42
# can be expressed as (a) 3+4+5+6+7+8+9, (b) 9+10+11+12, (c) 13+14+15 and (d) 42)

def count_consecutive_summers(num):
    """Count how many different ways an integer can be expressed as a sum of consecutive positive integers"""
    sum_variations = 1
    # sum_variations is initially 1 for the trivial sum that is simply the number itself
    for x in range(1, 1 + (num//2)):
        current_num = x
        current_sum = x
        while current_sum < num:
            current_num = current_num + 1
            current_sum = current_sum + current_num
        else:
            if current_sum == num:
                sum_variations +=1
    return sum_variations


if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 5
    assert count_consecutive_summers(1) == 1
