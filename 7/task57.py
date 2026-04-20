a = int(input())
b = int(input())

max_sum_dividers = 0
max_dividers_number = 0
for i in range(a, b + 1):
    sum_dividers = 0
    for j in range(1, i + 1):
        if i % j == 0:
            sum_dividers += j
    if sum_dividers >= max_sum_dividers:
        max_dividers_number = i
        max_sum_dividers = sum_dividers

print(max_dividers_number, max_sum_dividers)
