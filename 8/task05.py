n = int(input())

while n > 100:
    last_digit = n % 10
    n //= 10

print(last_digit)
