number = input()

if not 9 <= len(number) <= 10:
    print("NO")
elif (number[0] in "АВЕКМНОРСТУХ" and
      number[4] in "АВЕКМНОРСТУХ" and
      number[5] in "АВЕКМНОРСТУХ" and
      number[6] == "_" and
      number[1:4].isdigit() and
      number[7:].isdigit()):
    print("YES")
else:
    print("NO")
