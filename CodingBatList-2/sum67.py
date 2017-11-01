# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
def sum67(nums):
    sum = 0
    jump = False

    # iterate over nums
    for i, item in enumerate(nums):
        # See if you have already encountered a six and thus need to jump
        if jump == False:
            # If you see a 6, you need to start skipping values
            if nums[i] == 6:
               jump = True
            # If it is not a 6, you can add the value to the sum
            else:
                sum += nums[i]
        # If you are skipping values and you see a 7, end your jumps
        if nums[i] == 7:
            jump = False

    return sum


print(sum67([1, 2, 2]))
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1 , 1, 6, 7, 2]))
