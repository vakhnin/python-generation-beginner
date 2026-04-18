n = int(input())

for h in range(24):
    for m in range(60):
        if h ** n == m:
            if h < 10:
                print("0", end="")
            print(str(h) + ":",end="")
            if m < 10:
                print("0", end="")
            print(m)
