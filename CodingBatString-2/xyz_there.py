# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
import re
def xyz_there(str):
    # negative lookbehind assertion for . is (?<![.])
    # Searches str for an instance of xyz
    # that is not preceded by .
    if re.search('(?<![.])xyz',str) == None:
        return False

    return True


print(xyz_there('abcxyz'))
print(xyz_there('abc.xyz'))
print(xyz_there('xyz.abc'))
