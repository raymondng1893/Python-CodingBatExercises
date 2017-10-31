def sum2(nums):

    sum = 0

    if len(nums) == 0:
        sum = 0
    elif len(nums) == 1:
        sum = nums[0]
    else:
        sum = nums[0] + nums[1]

    return sum

print(sum2([1, 2, 3]))
print(sum2([1, 1]))
print(sum2([1, 1, 1, 1]))
