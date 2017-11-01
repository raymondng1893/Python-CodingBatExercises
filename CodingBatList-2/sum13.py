# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
def sum13(nums):
    sum = 0
    if len(nums) == 0:
        return sum
    else:
        for i, item in enumerate(nums):
            if nums[i] != 13:
                sum += nums[i]
            else:
                i += 2

    return sum


print(sum13([1, 2, 2, 1]))
print(sum13([1, 1]))
print(sum13([1, 2, 2, 1, 13]))
print(sum13([13, 13, 13, 13]))
