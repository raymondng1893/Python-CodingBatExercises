# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.
import re
def count_code(str):
    regex = re.compile("co[a-zA-z]e")
    count = re.findall(regex, str)
    return len(count)


print(count_code('aaacodebbb'))
print(count_code('codexxcode'))
print(count_code('cozexxcope'))
