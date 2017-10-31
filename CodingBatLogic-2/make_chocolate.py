def make_chocolate(small, big, goal):

    result = -1
    small_weight = 1
    big_weight = 5

    if small * small_weight + big * big_weight < goal:
        return result
    else:
        if goal % (big * big_weight) <= small * small_weight:
            result = goal % (big * big_weight)

    return result

print(make_chocolate(4, 1, 9))
print(make_chocolate(4, 1, 10))
print(make_chocolate(4, 1, 7))