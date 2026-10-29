# variant.py — вариант 11: числа с модулем не больше 3
# Лабораторная работа 6, индивидуальный вариант 11.
# Из ввода отбираются числа, для которых abs(number) <= 3.
# Повторы сохраняются, порядок исходный.
# Если подходящих чисел нет, результат [], количество 0,
# сумма 0, сортированная копия [].

line = input("Целые числа через пробел: ")

numbers = []
for part in line.split():
    numbers.append(int(part))

selected = []
for number in numbers:
    if abs(number) <= 3:
        selected.append(number)

print(f"Исходный список: {numbers}")
print(f"Подходящие числа: {selected}")
print(f"Количество: {len(selected)}")
print(f"Сумма: {sum(selected)}")
print(f"Отсортированная копия: {sorted(selected)}")
