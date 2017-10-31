def front_times(str, n):
    if len(str) < 3:
        return n*str
    else:
        return n*str[:3]

print(front_times('Chocolate',2))
print(front_times('Chocolate',3))
print(front_times('Abc',3))