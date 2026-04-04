from math import tan, pi

n, a = int(input()), float(input())

result = (n * (a ** 2)) / (4 * tan(pi / n))
print(result)
