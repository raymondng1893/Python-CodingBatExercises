import re
def count_hi(str):

    count = re.findall('hi', str)
    return len(count)

print(count_hi('abc hi ho'))
print(count_hi('ABChi hi'))
print(count_hi('hihi'))
