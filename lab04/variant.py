# variant.py — вариант 11: числа с модулем не больше 3
# Лабораторная работа 4, вариант 11.
# Один цикл: количество и сумма подходящих чисел. Список не используется.

n = int(input("Количество чисел (n >= 0): "))

count = 0
total = 0

for index in range(1, n + 1):
    value = int(input(f"Число {index}: "))
    if abs(value) <= 3:
        count += 1
        total += value

print(f"Количество: {count}")
print(f"Сумма: {total}")
