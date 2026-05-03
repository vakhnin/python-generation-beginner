n = int(input())

prev_data = input()
for i in range(n - 1):
    data = input()
    separator = " "
    if prev_data[:prev_data.find(separator)] > data[:prev_data.find(separator)]:
        print("NO")
        break
    if prev_data[:prev_data.find(separator)] == data[:data.find(separator)]:
        separator = "«"
        if prev_data[prev_data.find(separator) + 1:-1] > data[data.find(separator) + 1:-1]:
            print("NO")
            break
    prev_data = data
else:
    print("YES")
