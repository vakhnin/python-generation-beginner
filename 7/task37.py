number = int(input())

total, count, mult = 0, 0, 1
first_digit, last_digit = 0, 0
max_digit = 0
while number != 0:
    digit = number % 10
    total += digit
    count += 1
    mult *= digit
    if count == 1:
        last_digit = digit
    first_digit = digit
    number = number // 10

print(total)
print(count)
print(mult)
print(total / count)
print(first_digit)
print(first_digit + last_digit)
