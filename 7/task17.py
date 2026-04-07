n = int(input())

total = 0
for i in range(n + 1):
    last_digit = i ** 2 % 10
    if (last_digit == 2 or last_digit == 5
            or last_digit == 8):
        total += i
print(total)
