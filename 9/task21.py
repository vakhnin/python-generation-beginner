n = int(input())

count = 0
for _ in range(n):
    string = input()
    if string.count("11") >= 3:
        count += 1
print(count)
