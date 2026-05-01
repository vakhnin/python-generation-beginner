n = int(input())

for _ in range(n):
    class_number = input()
    if len(class_number) != 2:
        print("NO")
        continue
    if "0" <= class_number[0] <= "9" and "А" <= class_number[1] <= "П":
        print("YES")
    else:
        print("NO")
