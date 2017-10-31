def has23(nums):

    for i, item in enumerate(nums):
        if nums[i] == 2 or nums[i] == 3:
            return True

    return False

print(has23([2, 5]))
print(has23([4, 3]))
print(has23([4, 5]))
