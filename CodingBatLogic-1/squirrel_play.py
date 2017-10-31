def squirrel_play(temp, is_summer):

    summerleeway = 0

    if is_summer:
        summerleeway = 10

    if 60 <= temp <= 90 + summerleeway:
        return True

    return False

print(squirrel_play(70, False))
print(squirrel_play(95, False))
print(squirrel_play(95, True))
