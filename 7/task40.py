number = int(input())

digit = number % 10
ordered = "YES"
while number != 0:
    if digit > number % 10:
        ordered = "NO"
    digit = number % 10
    number = number // 10

print(ordered)
