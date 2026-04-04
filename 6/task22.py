from math import sqrt

x_1, y_1 = float(input()), float(input())
x_2, y_2 = float(input()), float(input())

result = sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)
print(result)
