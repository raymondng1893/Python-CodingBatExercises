def combo_string(a, b):

    if len(a) < len(b):
        short = a
        long = b
    else:
        short = b
        long = a

    return short + long + short

print(combo_string('Hello', 'hi'))
print(combo_string('hi', 'Hello'))
print(combo_string('aaa', 'b'))
print(combo_string('hi', 'hi'))
print(combo_string('', 'hi'))