# find the angle of the sun above the horizon. sun rises in the East at 6:00 AM, which corresponds to the angle of 0
# degrees. At 12:00 PM the sun reaches its zenith, which means that the angle equals 90 degrees. 6:00 PM is the time of
# the sunset so the angle is 180 degrees. If the input will be the time of the night (before 6:00 AM or after 6:00 PM),
# return - "I don't see the sun!"

# Note: not how calculating angles works IRL

def sun_angle(time):
    hour, minute = map(int,time.split(':'))
    total_minutes = hour*60 + minute
    if 6*60<=total_minutes<=18*60:
        degrees = (total_minutes-6*60)*(180/(12*60))
        return degrees
    else:
        return "I don't see the sun!"

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"