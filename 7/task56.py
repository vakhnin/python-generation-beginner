n = int(input())
m = int(input())

no_solve = True
for i in range(1, n):
    for j in range(1, n):
        for k in range(1, n):
            if i + 3 * j + 2 * k == m:
                no_solve = False
                j_mult = "3×" + str(j)
                k_mult = "2×" + str(k)
                print(i, "+", j_mult, "+", k_mult, "=", m)
if no_solve:
    print("При заданных n и m решений не существует.")
