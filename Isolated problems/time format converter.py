# convert the time from the 24-h format into 12-h format by following the next rules:
# - the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday)
# - if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'

def am_ify (time_list):
    return time_list[0] + ':' + time_list[1] + ' a.m.'

def pm_ify (time_list):
    return time_list[0] + ':' + time_list[1] + ' p.m.'

def time_converter(time):
    timesplit = time.split(':')
    hour_is_zero = int(timesplit[0]) == 0
    time_is_am = int(timesplit[0]) < 12
    hour_is_twelve = int(timesplit[0]) == 12
    pm_hour = int(timesplit[0]) - 12
    if hour_is_zero:
        timesplit[0] = '12'
        newtime = am_ify(timesplit)
    elif time_is_am:
        timesplit[0] = timesplit[0].lstrip('0')
        newtime = am_ify(timesplit)
    elif hour_is_twelve:
        newtime = pm_ify(timesplit)
    else:
        newtime = pm_ify([str(pm_hour),timesplit[1]])
    return newtime

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'