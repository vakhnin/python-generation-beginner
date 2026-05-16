n = int(input())

numbers = []
for _ in range(n):
    numbers.append(int(input()))

numbers.remove(max(numbers))
numbers.remove(min(numbers))

print(*numbers, sep="\n")
