# statistics.py — сумма, число положительных и максимум потока чисел
# Лабораторная работа 4, обязательное задание 2.
# Список не используется: значения обрабатываются по одному.
# Максимум инициализируется первым введённым числом, иначе все отрицательные
# значения дали бы неверный ответ при инициализации нулём.

n = int(input("Количество чисел (n >= 1): "))

first_value = int(input("Число 1: "))
total = first_value
positive_count = 1 if first_value > 0 else 0
maximum = first_value

for index in range(2, n + 1):
    value = int(input(f"Число {index}: "))
    total += value
    if value > 0:
        positive_count += 1
    if value > maximum:
        maximum = value

print(f"Сумма: {total}")
print(f"Положительных: {positive_count}")
print(f"Максимум: {maximum}")
