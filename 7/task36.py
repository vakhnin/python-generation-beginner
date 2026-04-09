number = int(input())

min_digit = 9
max_digit = 0
while number != 0:
    last_digit = number % 10
    min_digit = min(last_digit, min_digit)
    max_digit = max(last_digit, max_digit)
    number = number // 10

print("Максимальная цифра равна", max_digit)
print("Минимальная цифра равна", min_digit)
