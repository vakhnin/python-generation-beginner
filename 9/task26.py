string = input()

left = string.find("f")
right = string.rfind("f")

if left == -1:
    print("NO")
elif left == right:
    print(left)
else:
    print(left, right)
