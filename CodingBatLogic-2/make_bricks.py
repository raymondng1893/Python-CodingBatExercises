def make_bricks(small, big, goal):

    small_len = 1
    big_len = 5

    if big * big_len + small * small_len >= goal:
        if (goal % 5) <= small * small_len:
            return True

    return False

print(make_bricks(3, 1, 8))
print(make_bricks(3, 1, 9))
print(make_bricks(3, 2, 10))