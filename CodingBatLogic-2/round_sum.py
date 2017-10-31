def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

def round10(num):
    if num % 10 < 5:
       return int(num/10) * 10
    else:
        if int(num/10) == 0:
            return 10
        else:
            return int(num/10) * 2 * 10

print(round_sum(16, 17, 18))
print(round_sum(12, 13, 14))
print(round_sum(6, 4, 4))