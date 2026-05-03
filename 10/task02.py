n = int(input())

res = ""
for i in range(n):
    res += chr(ord("a") + i)
print(list(res))
