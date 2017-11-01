# Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.
def max_end3(nums):
    larger = 0

    if nums[0] >= nums[len(nums) - 1]:
        larger = nums[0]
    else:
        larger = nums[len(nums) - 1]

    # List comprehension with slice assignment
    # keeps existing references to the list
    nums[:] = [larger for i in nums]

    return nums


# # A different way to populate nums with the larger
# # value by using enumerate() to add a counter to
# # an iterable
# def max_end3(nums):
#
#     larger = 0
#
#     if nums[0] >= nums[len(nums) - 1]:
#         larger = nums[0]
#     else:
#         larger = nums[len(nums) - 1]
#
#     for i, item in enumerate(nums):
#         nums[i] = larger
#
#     return nums

print(max_end3([1, 2, 3]))
print(max_end3([11, 5, 9]))
print(max_end3([2, 11, 3]))
