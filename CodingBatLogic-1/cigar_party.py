def cigar_party(cigars, is_weekend):

    if is_weekend and cigars >= 40:
        return True
    elif not is_weekend and 40 <= cigars <= 60:
        return True

    return False

print(cigar_party(30 , False))
print(cigar_party(50, False))
print(cigar_party(70, True))
        