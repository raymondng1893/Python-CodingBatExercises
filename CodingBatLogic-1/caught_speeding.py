# You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
def caught_speeding(speed, is_birthday):
    result = 0
    bdayleeway = 0

    if is_birthday:
        bdayleeway = 5

    if 61 + bdayleeway <= speed <= 80 + bdayleeway:
        result = 1
    elif speed >= 81 + bdayleeway:
        result = 2

    return result


print(caught_speeding(60, False))
print(caught_speeding(65, False))
print(caught_speeding(65, True))
