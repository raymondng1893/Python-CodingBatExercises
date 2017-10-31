def non_start(a, b):
    tempa = ""
    tempb = ""

    if len(a) > 1:
        tempa = a[1:]

    if len(b) > 1:
        tempb = b[1:]

    return tempa + tempb

print(non_start('Hello', 'There'))
print(non_start('java', 'code'))
print(non_start('shotl','java'))
print(non_start('s', 'java'))
print(non_start('java', 't'))
print(non_start('s', 't'))