number = int(input())

a = number % 10
b = (number % 100) // 10
c = number // 100

print("Сумма цифр =", a + b + c)
print("Произведение цифр =", a * b * c)
