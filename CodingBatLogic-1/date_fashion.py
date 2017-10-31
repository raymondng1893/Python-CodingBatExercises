def date_fashion(you, date):

    # 0 = no, 1 = maybe, 2 = yes
    table_yes = 1

    if you <= 2 or date <= 2:
        table_yes = 0
    elif you >= 8 or date >= 8:
        table_yes = 2

    return table_yes

print(date_fashion(5, 10))
print(date_fashion(5, 2))
print(date_fashion(5, 5))
