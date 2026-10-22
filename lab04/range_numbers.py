# range_numbers.py — числа от a до b в нужном порядке
# Лабораторная работа 4, обязательное задание 1.
# При a < b — по возрастанию, при a > b — по убыванию, при равенстве — одно число.

a = int(input("Первое число: "))
b = int(input("Второе число: "))

print()

if a <= b:
    for number in range(a, b + 1):
        print(number)
else:
    for number in range(a, b - 1, -1):
        print(number)
