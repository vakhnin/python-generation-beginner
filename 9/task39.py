message = input()

count_ru = 0
count_en = 0
ru = "еуорахсЕТОРАНХСВМ"
en = "eyopaxcETOPAHXCBM"
for char in message:
    count_en += ord(char) * 3
    position = en.find(char)
    if position == -1:
        count_ru += ord(char) * 3
    else:
        count_ru += ord(ru[position]) * 3

print(f"Старая стоимость: {count_en}🐝")
print(f"Новая стоимость: {count_ru}🐝")
