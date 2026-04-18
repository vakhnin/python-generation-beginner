n = int(input())

factor = 1
result = 0
for i in range(1, n + 1):
    factor *= i
    result += factor

print(result)
