# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
def string_match(a, b):
    count = 0
    if len(a) > len(b):
        longer = a
        shorter = b
    else:
        longer = b
        shorter = a

    for i in range(0, len(shorter) - 1):
        if shorter[i:i + 2] == longer[i:i + 2]:
            count += 1

    return count


print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'abc'))
print(string_match('abc', 'axc'))
