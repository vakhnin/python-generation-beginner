n = int(input())

strings = []
for _ in range(n):
    strings.append(input())

k = int(input())
for current_string in strings:
    if k <= len(current_string):
        print(current_string[k - 1], end="")
