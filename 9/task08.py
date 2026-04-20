string = input()

last_char = string[0]
count_pair = 0
for i in range(1, len(string)):
    if string[i] == last_char:
        count_pair += 1
    last_char = string[i]
print(count_pair)
