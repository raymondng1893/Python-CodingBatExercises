def reverse3(nums):
    return list(reversed(nums))

print(reverse3([1, 2, 3]))
print(reverse3([5, 11, 9]))
print(reverse3([7, 0, 0]))


# With 3 parameters for the array e.g.
# nums[::-1], the 3rd parameter is step.
# In this case it goes 1 step backward all the way
# to the beginning

# def reverse3(nums):
#     return nums[::-1]
#
# print(reverse3([1, 2, 3]))
# print(reverse3([5, 11, 9]))
# print(reverse3([7, 0, 0]))
