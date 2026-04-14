number = int(input())

first_digit = number % 10
all_equal = True
while number != 0:
    if first_digit != number % 10:
        all_equal = False
    number = number // 10

if all_equal:
    print("YES")
else:
    print("NO")
