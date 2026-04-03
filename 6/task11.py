number_1, number_2, number_3 = int(input()), int(input()), int(input())

min_number = min(number_1, number_2, number_3)
max_number = max(number_1, number_2, number_3)
midle_number = number_1 + number_2 + number_3 - min_number - max_number

print(max_number)
print(midle_number)
print(min_number)
