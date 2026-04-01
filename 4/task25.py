number = int(input())

if 0 <= number <= 36:
    if number == 0:
        print("зеленый")
    else:
        if 1 <= number <= 10 or 19 <= number <= 28:
            number += 1
        if number % 2:
            print("черный")
        else:
            print("красный")
else:
    print("ошибка ввода")
