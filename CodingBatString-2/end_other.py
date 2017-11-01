# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.
import re
def end_other(a, b):
    if len(a) <= len(b):
        if re.match(a, b[len(b) - len(a):], re.IGNORECASE):
            return True
    elif len(b) <= len(a):
        if re.match(b, a[len(a) - len(b):], re.IGNORECASE):
            return True

    return False


print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))
print(end_other('abc', 'ab'))
