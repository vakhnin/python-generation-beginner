string = input()

has_digit = "Цифр нет"
for char in string:
    if char in "0123456789":
        has_digit = "Цифра"
        break

print(has_digit)
