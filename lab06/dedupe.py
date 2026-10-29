# dedupe.py — удаление повторов без set
# Лабораторная работа 6, дополнительное задание.
# Повторы удаляются, сохраняется порядок первого появления.
# Проверка вхождения выполняется по уже собранному списку,
# поэтому set не используется.

line = input("Целые числа через пробел: ")

numbers = []
for part in line.split():
    numbers.append(int(part))

unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)

print(f"Исходный список: {numbers}")
print(f"Без повторов: {unique}")
