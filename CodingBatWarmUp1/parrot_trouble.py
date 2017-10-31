def parrot_trouble(talking, hour):
    if talking and (0 <= hour < 7 or 20 < hour <= 23):
        return True
    else:
        return False

print(parrot_trouble(True, 6))
print(parrot_trouble(True, 7))
print(parrot_trouble(False, 6))
print(parrot_trouble(True, -1))


