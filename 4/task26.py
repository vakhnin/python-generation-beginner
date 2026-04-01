a_1, b_1 = int(input()), int(input())
a_2, b_2 = int(input()), int(input())

if a_1 > a_2:
    left = a_1
else:
    left = a_2

if b_1 < b_2:
    right = b_1
else:
    right = b_2

if left < right:
    print(left, right)
elif left == right:
    print(left)
else:
    print("пустое множество")
