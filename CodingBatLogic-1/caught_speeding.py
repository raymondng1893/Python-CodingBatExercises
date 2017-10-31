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