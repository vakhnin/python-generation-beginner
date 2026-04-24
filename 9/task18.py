string = input()

count = 0
for char in string:
    if char in "abcdefghijklmnopqrstuvwxyz":
        count += 1

print(count)
