def first_two(str):

    if len(str) < 2:
        return str
    else:
        return str[:2]

print(first_two('Hello'))
print(first_two('abcdefg'))
print(first_two('ab'))
print(first_two('X'))