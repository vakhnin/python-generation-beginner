n = int(input())

res = []
for _ in range(n):
    res.append(int(input()))
del res[1::2]

print(res)
