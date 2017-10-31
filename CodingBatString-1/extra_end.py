def extra_end(str):
    start = len(str) - 2

    return 3*str[start:]

print(extra_end('Hello'))
print(extra_end('ab'))
print(extra_end('Hi'))