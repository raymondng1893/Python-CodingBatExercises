def lucky_sum(a, b, c):

    sum = a + b + c

    if a == 13:
        sum = 0
    elif b == 13:
        sum = a
    elif c == 13:
        sum = a + b

    return sum

print(lucky_sum(1, 2, 3))
print(lucky_sum(1, 2, 13))
print(lucky_sum(1, 13, 3))