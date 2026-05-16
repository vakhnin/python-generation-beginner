n = int(input())

negatives, zeros, positives = [], [], []
for _ in range(n):
    num = int(input())
    if num == 0:
        zeros.append(num)
    elif num < 0:
        negatives.append(num)
    else:
        positives.append(num)

result = negatives
result.extend(zeros)
result.extend(positives)

for num in result:
    print(num)
