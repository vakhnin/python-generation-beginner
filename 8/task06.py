n = int(input())

digit = n % 10
count_3 = 0
last_digit = n % 10
count_last_digit = 0
count_even = 0
total_more_then_5 = 0
mult_more_then_7 = 1
count_0_5 = 0
while n > 0:
    digit = n % 10
    if digit == 3:
        count_3 += 1
    if digit == last_digit:
        count_last_digit += 1
    if digit % 2 == 0:
        count_even += 1
    if digit > 5:
        total_more_then_5 += digit
    if digit > 7:
        mult_more_then_7 *= digit
    if digit == 0:
        count_0_5 += 1
    if digit == 5:
        count_0_5 += 1
    n //= 10
print(count_3)
print(count_last_digit)
print(count_even)
print(total_more_then_5)
print(mult_more_then_7)
print(count_0_5)
