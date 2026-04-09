n = int(input())

count = n // 25
count_total = count
n -= count * 25

count = n // 10
count_total += count
n -= count * 10

count = n // 5
count_total += count
n -= count * 5

count_total += n

print(count_total)
