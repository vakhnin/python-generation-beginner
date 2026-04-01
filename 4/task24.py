color_1, color_2 = input(), input()

if color_1 == "красный" or color_2 == "красный":
    if color_1 == color_2:
        print("красный")
    elif color_1 == "синий" or color_2 == "синий":
        print("фиолетовый")
    elif color_1 == "желтый" or color_2 == "желтый":
        print("оранжевый")
    else:
        print("ошибка цвета")
elif color_1 == "синий" or color_2 == "синий":
    if color_1 == "красный" or color_2 == "красный":
        print("фиолетовый")
    elif color_1 == color_2:
        print("синий")
    elif color_1 == "желтый" or color_2 == "желтый":
        print("зеленый")
    else:
        print("ошибка цвета")
elif color_1 == "желтый" or color_2 == "желтый":
    if color_1 == "красный" or color_2 == "красный":
        print("оранжевый")
    elif color_1 == "синий" or color_2 == "синий":
        print("зеленый")
    elif color_1 == color_2:
        print("желтый")
    else:
        print("ошибка цвета")
else:
    print("ошибка цвета")
