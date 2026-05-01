str_1, str_2, str_3 = input(), input(), input()

str_min = min(str_1, str_2, str_3)
str_max = max(str_1, str_2, str_3)

print(str_min, end=" ")
for current_str in (str_1, str_2, str_3):
    if current_str != str_min and current_str != str_max:
        print(current_str, end=" ")
        break
print(str_max)
