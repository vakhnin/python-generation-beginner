day, weight = int(input()), float(input())

weight_one_day = (100 - 88) / 60

weight_plan = 100 - weight_one_day * day
if weight <= weight_plan:
    print("Все идет по плану")
else:
    print("Что-то пошло не так")
print(f"#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {weight_plan} кг")
