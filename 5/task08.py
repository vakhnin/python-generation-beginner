x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

sub_x, sub_y = x_2 - x_1, y_2 - y_1

if abs(x_2 - x_1) == abs(y_2 - y_1) or x_1 == x_2 or y_1 == y_2:
    print("YES")
else:
    print("NO")
