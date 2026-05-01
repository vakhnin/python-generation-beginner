message = input()

start_index = 0
char_start = message.find("[u-", start_index)
char_end = 0
while True:
    if char_start == -1:
        print(message[char_end:], end="")
        break
    else:
        print(message[char_end:char_start], end="")
        char_end = message.find("]", char_start + 1)
        print(chr(int(message[char_start + 3:char_end])), end="")
        char_end += 1
        start_index = char_end
    char_start = message.find("[u-", start_index)
