n = int(input())

last = int(input())
res = []
for _ in range(n - 1):
    current = int(input())
    res.append(last + current)
    last = current

print(res)
