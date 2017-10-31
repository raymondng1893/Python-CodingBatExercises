def in1to10(n, outside_mode):

    if outside_mode:
        if n <= 1 or n >= 10:
            return True

    if 1 <= n <= 10:
        return True

    return False

print(in1to10(5, False))
print(in1to10(11, False))
print(in1to10(11, True))