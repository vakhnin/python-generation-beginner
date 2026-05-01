str_1, str_2 = input(), input()
str_new_1, str_new_2 = "", ""

for char in str_1:
    if char.isalpha():
        str_new_1 += char

for char in str_2:
    if char.isalpha():
        str_new_2 += char

if str_new_1.lower() == str_new_2.lower():
    print("YES")
else:
    print("NO")
