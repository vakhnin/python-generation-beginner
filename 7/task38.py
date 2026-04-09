number = int(input())

last_digit = number % 10
while number != 0:
    second_digit = last_digit
    last_digit = number % 10
    number = number // 10
print(second_digit)
