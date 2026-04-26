nickname = input()

if (5 <= len(nickname) <= 15 and nickname[0] == "@" and
    nickname[1:].isalnum()) and nickname == nickname.lower():
    print("Correct")
else:
    print("Incorrect")
