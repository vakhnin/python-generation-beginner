string = input()

count_plus = 0
count_mult = 0
for char in string:
    if char == "+":
        count_plus += 1
    if char == "*":
        count_mult += 1

print("Символ + встречается", count_plus, "раз")
print("Символ * встречается", count_mult, "раз")
