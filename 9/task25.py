string = input()

max_count = -1
max_char = ""

for char in string:
    if string.count(char) >= max_count:
        max_char = char
        max_count = string.count(char)

print(max_char)
