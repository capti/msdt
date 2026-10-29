# functions.py — функции лабораторной работы 7
# Ни одна функция не вызывает input() и print(): данные приходят
# параметрами, результат уходит через return.

def sum_digits(number):
    """Вернуть сумму цифр модуля number; для нуля — 0."""
    rest = abs(number)
    total = 0
    while rest > 0:
        total += rest % 10
        rest = rest // 10
    return total


def average(numbers):
    """Вернуть среднее значение списка, для пустого списка — None."""
    if len(numbers) == 0:
        return None
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


def normalize_text(text):
    """Вернуть строку в нижнем регистре: края без пробелов,
    между словами один пробел."""
    return " ".join(text.lower().split())


def select_numbers(numbers, threshold):
    """Вариант 11: вернуть новый список чисел с abs(number) == threshold.
    Порядок и повторы сохраняются, исходный список не меняется."""
    selected = []
    for number in numbers:
        if abs(number) == threshold:
            selected.append(number)
    return selected


def is_palindrome(text):
    """Дополнительно: True, если нормализованный текст без пробелов
    читается одинаково в обе стороны; для пустого текста — False."""
    normalized = normalize_text(text)
    if normalized == "":
        return False
    cleaned = normalized.replace(" ", "")
    return cleaned == cleaned[::-1]
