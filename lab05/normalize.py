# normalize.py — нормализация текста
# Лабораторная работа 5, обязательное задание 1.
# Пробелы по краям убираются, последовательности внутри сжимаются до одного.
# Регистр сохраняется.

text = input("Введите текст: ")

normalized = " ".join(text.split())
words_count = len(normalized.split())

print(f"Исходная длина: {len(text)}")
print(f"Новая длина: {len(normalized)}")
print(f"Нормализованный текст: {normalized}")
print(f"Слов: {words_count}")
