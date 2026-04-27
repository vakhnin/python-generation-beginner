message = input()

count = 0
for char in message:
    count += ord(char) * 3

print(f"Текст сообщения: '{message}'")
print(f"Стоимость сообщения: {count}🐝")
