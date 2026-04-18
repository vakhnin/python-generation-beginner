n = int(input())

for i in range(1, n + 2):
    for j in range(1, i):
        print(j, end="")
    for j in range(i - 2, 0, -1):
        print(j, end="")
    print()
