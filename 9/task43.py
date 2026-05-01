text = input()
min_str = text
max_str = text
while text != "КОНЕЦ":
    min_str = min(min_str, text)
    max_str = max(max_str, text)
    text = input()

print(f"Минимальная строка ⬇️: {min_str}")
print(f"Максимальная строка ⬆️: {max_str}")
