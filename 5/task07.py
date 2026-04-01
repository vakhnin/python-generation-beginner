x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

if (abs(x_2 - x_1) == 1 and abs(y_2 - y_1) == 2
        or abs(x_2 - x_1) == 2 and abs(y_2 - y_1) == 1):
    print("YES")
else:
    print("NO")
