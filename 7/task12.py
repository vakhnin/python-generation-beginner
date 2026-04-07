m, n = int(input()), int(input())

for i in range(m - 1 + m % 2, n - 1, -2):
    print(i)
