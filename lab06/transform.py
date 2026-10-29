# transform.py — независимое преобразование списка
# Лабораторная работа 6, обязательное задание 2.
# Строится новый список, в котором отрицательные числа
# заменены модулями. Исходный список не изменяется.
# Пустой ввод даёт два пустых списка.

line = input("Целые числа через пробел: ")

numbers = []
for part in line.split():
    numbers.append(int(part))

transformed = []
for number in numbers:
    if number < 0:
        transformed.append(-number)
    else:
        transformed.append(number)

print(f"Исходный список: {numbers}")
print(f"Новый список: {transformed}")
print(f"Исходный список после преобразования: {numbers}")
