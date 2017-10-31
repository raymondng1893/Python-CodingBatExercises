def lone_sum(a, b, c):

    sum = a + b + c

    if a == b == c:
        sum = 0
    elif a == b:
        sum = c
    elif a == c:
        sum = b
    elif b == c:
        sum = a

    return sum

print(lone_sum(1, 2, 3))
print(lone_sum(3, 2, 3))
print(lone_sum(3, 3, 3))