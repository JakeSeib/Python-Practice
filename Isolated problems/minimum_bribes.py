# It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued
# up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by 1
# from 1 at the front of the line to n at the back.
#
# Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap
# positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two
# others. For example, if n = 8 and Person 5 bribes Person 4, the queue will look like this: 1,2,3,5,4,6,7,8.
#
# Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the
# queue into its current state!
#
# Function Description
#
# Complete the function minimumBribes in the editor below. It must print an integer representing the minimum number of
# bribes necessary, or Too chaotic if the line configuration is not possible.
#
# minimumBribes has the following parameter(s):
#
# q: an array of integers

def minimumBribes(q):
    # for one person, naively, bribes given/taken is starting index - final index
    # however, a person can both give and take bribes, i.e.
    # 1,2,3 => 2,1,3 => 2,3,1 => 3,2,1
    # 3 is 2 positions ahead, 1 is 2 positions behind, but there were 3 bribes
    # key for this situation is that we can tell a 3rd bribe was given because 2 is ahead of 1
    # so # of bribes is really # of people behind an individual who started out in front of them
    # in this case, 3 has 2, and 2 has 1 => 3 total
    bribes = 0
    visited = set()
    for index in range(0, len(q)):
        person = q[index]
        visited.add(person)
        curr_person_visited = visited.copy()
        curr_person_bribes = 0
        # start looking at everyone behind person, until we've found everyone who started in front of person
        for other in q[index + 1:]:
            # check if everyone starting in front of person is accounted for
            if set([x for x in range(1, person)]).issubset(curr_person_visited):
                break
            curr_person_visited.add(other)
            if other < person:
                bribes += 1
                curr_person_bribes += 1
                if curr_person_bribes > 2:
                    return 'Too chaotic'
    return bribes

print(minimumBribes([2, 1, 5, 3, 4]))
print(minimumBribes([2, 5, 1, 3, 4]))
print(minimumBribes([5, 1, 2, 3, 7, 8, 6, 4]))
