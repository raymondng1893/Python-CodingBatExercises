def alarm_clock(day, vacation):

    clocktime = ""
    weekday = False
    if 1 <= day <= 5:
        weekday = True

    if vacation:
        if weekday:
            clocktime = "10:00"
        else:
            clocktime = "off"
    else:
        if weekday:
            clocktime = "7:00"
        else:
            clocktime = "10:00"

    return clocktime

print(alarm_clock(1, False))
print(alarm_clock(5, False))
print(alarm_clock(0, False))
