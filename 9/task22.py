string = input()

count = 0
for char in string:
    if char in "0123456789":
        count += 1
print(count)
