number_1, number_2 = int(input()), int(input())
number_3, number_4 = int(input()), int(input())

minimum = number_1
if number_2 < minimum:
    minimum = number_2
if number_3 < minimum:
    minimum = number_3
if number_4 < minimum:
    minimum = number_4
print(minimum)