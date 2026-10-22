# replace.py — замена двоеточий на дефисы с подсчётом
# Лабораторная работа 5, обязательное задание 3.
# Сначала количество вхождений в исходной строке, затем сама замена.

text = input("Введите текст: ")

replacements_count = text.count(":")
new_text = text.replace(":", "-")

print(f"Замен: {replacements_count}")
print(f"Результат: {new_text}")
