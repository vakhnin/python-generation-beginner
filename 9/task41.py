n = int(input())
message = input()

for char in message:
    decrypt_char = ord(char) - n
    if decrypt_char < 97:
        decrypt_char += 26
    print(chr(decrypt_char), end="")
