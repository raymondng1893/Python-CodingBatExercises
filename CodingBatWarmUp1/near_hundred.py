# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number
def near_hundred(n):
    if abs(n-100) <= 10:
        return True
    elif abs(n-200) <= 10:
        return True
    else:
        return False


print(near_hundred(93))
print(near_hundred(90))
print(near_hundred(89))
print(near_hundred(190))
print(near_hundred(210))

# Other solution
# def near_hundred(n):
# return((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
