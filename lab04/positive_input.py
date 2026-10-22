# positive_input.py — повторный ввод до положительного числа
# Лабораторная работа 4, обязательное задание 3.
# Тип int гарантируется, поэтому проверяется только знак числа.

number = int(input("Введите целое число: "))
rejected_count = 0

while number <= 0:
    rejected_count += 1
    number = int(input("Число должно быть положительным, повторите: "))

print(f"Квадрат числа: {number ** 2}")
print(f"Отклонено попыток: {rejected_count}")
