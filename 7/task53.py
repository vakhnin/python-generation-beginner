n = int(input())

current_number = 1
columns = 1
while True:
    for _ in range(1, columns):
        print(current_number, end=" ")
        current_number += 1
    if columns > n:
        break
    columns += 1
    print()
