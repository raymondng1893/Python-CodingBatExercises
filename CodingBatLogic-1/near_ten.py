# Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2.
def near_ten(num):
    if num  % 10 <= 2 or num % 10 >= 8:
        return True

    return False


print(near_ten(12))
print(near_ten(17))
print(near_ten(19))
print(near_ten(28))
print(near_ten(27))
