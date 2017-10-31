import re

def count_code(str):
    regex = re.compile("co[a-zA-z]e")
    count = re.findall(regex, str)
    return len(count)

print(count_code('aaacodebbb'))
print(count_code('codexxcode'))
print(count_code('cozexxcope'))