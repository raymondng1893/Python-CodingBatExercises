# Finds the middle values of two odd arrays and
# returns both in a new array

def middle_way(a, b):
    result = []
    result.append(a[int(len(a)/2)])
    result.append(b[int(len(b)/2)])

    return result

print(middle_way([1, 2, 3], [4, 5, 6]))
print(middle_way([7, 7, 7], [3, 8, 0]))
print(middle_way([5, 2, 9], [1, 4, 5]))
print(middle_way([5, 2, 9, 4, 6], [1, 4, 3]))

