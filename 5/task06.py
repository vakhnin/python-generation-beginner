x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

sub_x, sub_y = x_2 - x_1, y_2 - y_1

if abs(x_2 - x_1) == abs(y_2 - y_1):
    print("YES")
else:
    print("NO")
