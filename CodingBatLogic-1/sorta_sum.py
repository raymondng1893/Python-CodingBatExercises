def sorta_sum(a, b):

    sum = 0

    if 10 <= a + b <= 19:
        sum = 20
    else:
        sum = a + b

    return sum

print(sorta_sum(3, 4))
print(sorta_sum(9, 4))
print(sorta_sum(10, 11))