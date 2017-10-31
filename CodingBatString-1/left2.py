def left2(str):
    leftchars = str[:2]

    return str[2:] + leftchars

print(left2('Hello'))
print(left2('java'))
print(left2('Hi'))
