# Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.
def without_end(str):
    end = len(str) - 1

    return str[1:end]


print(without_end('Hello'))
print(without_end('java'))
print(without_end('coding'))
