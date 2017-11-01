# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
def has22(nums):
    for i, item in enumerate(nums):
        if nums[i] == 2 and i + 1 < len(nums):
            if nums[i + 1] == 2:
                return True
        else:
            continue

    return False


print(has22([1, 2, 2]))
print(has22([1, 2, 1, 2]))
print(has22([2, 1, 2]))
