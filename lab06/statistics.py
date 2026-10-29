# statistics.py — статистика по списку чисел
# Лабораторная работа 6, обязательное задание 1.
# Вводятся целые числа одной строкой.
# При пустом вводе выводится только "Нет данных",
# min(), max() и деление на ноль не вызываются.

line = input("Целые числа через пробел: ")

numbers = []
for part in line.split():
    numbers.append(int(part))

if len(numbers) == 0:
    print("Нет данных")
else:
    total = sum(numbers)
    print(f"Количество: {len(numbers)}")
    print(f"Сумма: {total}")
    print(f"Минимум: {min(numbers)}")
    print(f"Максимум: {max(numbers)}")
    print(f"Среднее: {total / len(numbers):.2f}")
