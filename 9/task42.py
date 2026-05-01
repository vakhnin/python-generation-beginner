string_1, string_2 = input(), input()
string_3, string_4 = input(), input()

min_str = min(string_1, string_2, string_3, string_4)
max_str = max(string_1, string_2, string_3, string_4)

magic_number = (ord(min_str[-1]) * ord(max_str[-1])) ** 2
print(magic_number)
