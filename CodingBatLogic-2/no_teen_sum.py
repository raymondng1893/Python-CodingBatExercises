def fix_teen(n):
    result = n

    if 13 <= n <= 19:
        if n == 15:
            result = 15
        elif n == 16:
            result = 16
        else:
            result = 0

    return result


def no_teen_sum(a, b, c):

    return fix_teen(a) + fix_teen(b) + fix_teen(c)

print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))
