def rotate_left3(nums):

    result = []

    # Shifts the list left using slices
    # e.g. [1, 2, 3]
    # nums[1:] gives 2, 3
    # nums[:1] gives nums[0] = 1
    # result = 2, 3 + 1 = [2, 3, 1]
    result = nums[1:] + nums[:1]

    return result

print(rotate_left3([1, 2, 3]))
print(rotate_left3([5, 11, 9]))
print(rotate_left3([7, 0, 0]))