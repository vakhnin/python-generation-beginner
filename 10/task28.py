n = int(input())

messages = []
for _ in range(n):
    messages.append(input())

k = int(input())

searches = []
for _ in range(k):
    searches.append(input())

for message in messages:
    for search in searches:
        if search.lower() not in message.lower():
            break
    else:
        print(message)
