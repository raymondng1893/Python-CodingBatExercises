def string_splosion(str):
    final = ""
    for i in range(len(str)):
        final = final + str[:i+1]

    return final

print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))