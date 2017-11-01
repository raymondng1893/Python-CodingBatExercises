# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".
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
