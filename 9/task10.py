number = int(input())

result = ""
while number > 0:
    if number % 2 == 0:
        result = "0" + result
    else:
        result = "1" + result
    number //= 2
print(result)
