# An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly 'steps' steps, for every step
# it was noted if it was an uphill, U, or a downhill, D step. Hikes always start and end at sea level, and each step up or
# down represents a  unit change in altitude. We define the following terms:
#
# A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with
# a step down to sea level.
# A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with
# a step up to sea level.
# Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.
#
# Example
# steps = 8 path = [DDUUUUDD]
#
# The hiker first enters a valley 2 units deep. Then they climb out and up onto a mountain 2 units high. Finally, the
# hiker returns to sea level and ends the hike.

def countingValleys(steps, path):
    # map from path to elevation at each step, starting with 0
    elevations = [0]
    for step in path:
        step_value = 1 if step == 'U' else -1
        elevations.append(elevations[-1] + step_value)
    # look over elevations for segments all < 0 for valleys
    valleys = 0
    in_valley = False
    for index in range(0, len(elevations)):
        if elevations[index] < 0:
            if in_valley == False:
                valleys += 1
                in_valley = True
        # at 0, swap over in_valley
        elif elevations[index] == 0 and in_valley == True:
            in_valley = False
    return valleys

print(countingValleys(8, 'DDUUUUDDDU'))