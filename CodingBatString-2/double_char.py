def double_char(str):

    result = ""

    for i, item in enumerate(str):
        result += 2*str[i]

    return result

print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi-There'))
