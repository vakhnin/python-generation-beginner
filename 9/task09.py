string = input()

count_glas = 0
count_not_glas = 0
for char in string:
    if char in "ауоыиэяюеАУОЫИЭЯЮЕ":
        count_glas += 1
    if char in "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ":
        count_not_glas += 1

print("Количество гласных букв равно", count_glas)
print("Количество согласных букв равно", count_not_glas)
