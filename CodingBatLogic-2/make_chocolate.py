# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.
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
