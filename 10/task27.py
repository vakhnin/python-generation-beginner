n = int(input())

messages = []
for _ in range(n):
    messages.append(input())
search = input()

for message in messages:
    if search.lower() in message.lower():
        print(message)
