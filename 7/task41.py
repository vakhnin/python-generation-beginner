number = int(input())

counter = 0
number_len = len(str(number))
for i in range(1, number_len + 1):
    digit = (number // 10 ** (number_len - i)) % 10
    if digit % 2 == 0:
        counter += 1
        print(counter, end="")
        print("-я четная цифра равна", digit)

if counter == 0:
    print("Четных цифр в числе нет")
