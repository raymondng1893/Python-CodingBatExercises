def make_ends(nums):

    result = []

    result.append(nums[0])
    result.append(nums[len(nums) - 1])

    return result

print(make_ends([1, 2, 3]))
print(make_ends([1, 2, 3, 4]))
print(make_ends([7, 4, 6, 2]))