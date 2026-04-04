from math import sqrt

a, b, c = float(input()), float(input()), float(input())

d = b ** 2 - 4 * a * c

if d < 0:
    print("Нет корней")
elif d == 0:
    print(-b / (2 * a))
else:
    x_1 = (-b - sqrt(d)) / (2 * a)
    x_2 = (-b + sqrt(d)) / (2 * a)
    print(min(x_1, x_2))
    print(max(x_1, x_2))
