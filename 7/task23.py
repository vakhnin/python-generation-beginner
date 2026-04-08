n = int(input())

fib_1 = 1
fib_2 = 1
for _ in range(n):
    print(fib_1, end=" ")
    fib_1, fib_2 = fib_2, fib_1 + fib_2
