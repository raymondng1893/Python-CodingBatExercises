# Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
def missing_char(str, n):
    if str != '' and (0 <= n <= len(str)-1):
        newstr = str[0:n] + str[n+1:len(str)]
        return newstr
    else:
        return


print(missing_char('kitten', 1))
print(missing_char('kitten', 0))
print(missing_char('kitten', 4))
print(missing_char('', 1))
print(missing_char('kitten', 7))
