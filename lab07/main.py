# main.py — демонстрация функций из functions.py
# Лабораторная работа 7: ввод данных и вывод результата отделены
# от вычислений, все вычисления выполняют функции из модуля.

from functions import (
    average,
    is_palindrome,
    normalize_text,
    select_numbers,
    sum_digits,
)


def main():
    # Задание 1: сумма цифр
    number = int(input("Целое число: "))
    print(f"Сумма цифр модуля: {sum_digits(number)}")

    # Задание 2: среднее по строке чисел
    line = input("Строка чисел через пробел: ")
    numbers = []
    for part in line.split():
        numbers.append(int(part))
    mean = average(numbers)
    if mean is None:
        print("Среднее: Нет данных")
    else:
        print(f"Среднее: {mean}")

    # Задание 3: нормализация текста
    text = input("Произвольный текст: ")
    print(f"Нормализованный текст: {normalize_text(text)!r}")

    # Индивидуальный вариант 11: отбор по модулю, равному порога
    threshold = int(input("Порог (целое неотрицательное): "))
    selected = select_numbers(numbers, threshold)
    print(f"Исходный список: {numbers}")
    if len(selected) == 0:
        print("Подходящих чисел нет")
    else:
        print(f"Подошли (модуль равен {threshold}): {selected}")

    # Дополнительно: проверка на палиндром
    print(f"Палиндром: {is_palindrome(text)}")


if __name__ == "__main__":
    main()
