number = int(input())

d_1 = (number // 10 ** 2) % 10
d_2 = (number // 10 ** 1) % 10
d_3 = (number // 10 ** 0) % 10

min_digit = min(d_1, d_2, d_3)
max_digit = max(d_1, d_2, d_3)
midle_digit = d_1 + d_2 + d_3 - min_digit - max_digit

if max_digit - min_digit == midle_digit:
    print("Число интересное")
else:
    print("Число неинтересное")
