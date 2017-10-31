import re
def cat_dog(str):
    catcount = re.findall('cat', str)
    dogcount = re.findall('dog', str)

    return len(catcount) == len(dogcount)

print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))