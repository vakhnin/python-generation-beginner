n = int(input())

result = []
for _ in range(n):
    current = input()
    if current not in result:
        result.append(current)
print(*result, sep="\n")
