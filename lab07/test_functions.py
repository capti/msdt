# test_functions.py — проверки функций из functions.py
# Запуск: python test_functions.py
# При неудаче assert бросает AssertionError и программа останавливается.

from functions import (
    average,
    is_palindrome,
    normalize_text,
    select_numbers,
    sum_digits,
)

# --- Базовые проверки из задания ---

assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""
print("Базовые проверки пройдены")

# --- Вариант 11: контрольный список [-5, 0, 2, 5], порог 2 ---

source = [-5, 0, 2, 5]
saved = source.copy()
assert select_numbers(source, 2) == [2]
assert select_numbers([1, 3, 7, -7], 2) == []   # пустая выборка
assert select_numbers([], 2) == []              # пустой список
assert select_numbers(source, 0) == [0]         # только ноль равен 0
print("Контрольный список пройден")

# --- Граница условия: модуль ровно равен порогу ---

assert select_numbers([-2, 2, -3, 3, 1], 2) == [-2, 2]  # 2 и -2 проходят
assert select_numbers([-3, 3], 2) == []                 # 3 и -3 не проходят
assert select_numbers([-2, 2, -3, 3, 1], 0) == []       # единица не равна 0
assert select_numbers([0], 0) == [0]                     # 0 == 0
# Для варианта 11 при пороге 0 совпадает только само число 0
print("Границы условия пройдены")

# --- Повторы подходящего значения сохраняются ---

assert select_numbers([2, -2, 2, 5, -2], 2) == [2, -2, 2, -2]
print("Повторы пройдены")

# --- Порядок исходный и список не изменяется ---

assert source == saved
assert select_numbers([5, -5, 0, 2], 2) == [2]
print("Исходный список не изменён")

# --- Проверки до реализации is_palindrome (дополнительно) ---

assert is_palindrome("А роза упала на лапу Азора") is True
assert is_palindrome("    ") is False            # пустой нормализованный текст
assert is_palindrome("") is False
assert is_palindrome("   НЕТ   ") is False
assert is_palindrome("Палиндром") is False
print("Проверки палиндрома пройдены")

print("Все проверки пройдены")
