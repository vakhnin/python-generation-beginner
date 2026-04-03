str_1, str_2, str_3 = input(), input(), input()

min_len = min(len(str_1), len(str_2), len(str_3))
max_len = max(len(str_1), len(str_2), len(str_3))
midle_len = len(str_1) + len(str_2) + len(str_3) - min_len - max_len

if max_len - midle_len == midle_len - min_len:
    print("YES")
else:
    print("NO")
