# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;
def last2(str):
    count = 0
    end = str[-2:]

    for i in range(0, len(str) - 2):
        if str[i:i+2] == end:
            count += 1

    return count


print(last2('hixxhi'))
print(last2('xaxxaxaxx'))
print(last2('axxxaaxx'))
