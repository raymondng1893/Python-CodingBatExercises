# Given a string, return a new string where the first and last chars have been exchanged.
def front_back(str):
    if len(str) <= 1:
        return str
    else:
        front = str[0]
        back = str[len(str)-1]
        return back + str[1:len(str)-1] + front


print(front_back('code'))
print(front_back('a'))
print(front_back('ab'))
