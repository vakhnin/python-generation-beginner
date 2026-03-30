number = int(input())

d1 = (number // 10 ** 3) % 10
d2 = (number // 10 ** 2) % 10
d3 = (number // 10 ** 1) % 10
d4 = (number // 10 ** 0) % 10

if d1 + d4 == d2 - d3:
    print("ДА")
else:
    print("НЕТ")
