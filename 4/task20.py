x, y, z = int(input()), int(input()), int(input())

if y < x < z or z < x < y:
    print(x)
if x < y < z or z < y < x:
    print(y)
if x < z < y or y < z < x:
    print(z)
