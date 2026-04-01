x, y, op = int(input()), int(input()), input()

if op == "+":
    print(x + y)
elif op == "-":
    print(x - y)
elif op == "*":
    print(x * y)
elif op == "/":
    if y == 0:
        print("На ноль делить нельзя!")
    else:
        print(x / y)
else:
    print("Неверная операция")
