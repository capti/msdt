# positions.py — позиции максимального элемента
# Лабораторная работа 6, обязательное задание 3.
# Собираются все индексы максимального элемента
# в порядке возрастания через enumerate().
# Для пустого списка выводится "Нет данных".

line = input("Целые числа через пробел: ")

numbers = []
for part in line.split():
    numbers.append(int(part))

if len(numbers) == 0:
    print("Нет данных")
else:
    maximum = max(numbers)
    positions = []
    for index, value in enumerate(numbers):
        if value == maximum:
            positions.append(index)
    print(f"Максимум: {maximum}")
    print(f"Позиции: {positions}")
