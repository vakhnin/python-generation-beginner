n = int(input())

numbers = []
for _ in range(n):
    numbers.append(int(input()))
print(*numbers, sep="\n")

print()
for x in numbers:
    print(x ** 2 + 2 * x + 1)
