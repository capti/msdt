# variant.py — вариант 11: слова длиной от 3 до 5
# Лабораторная работа 5, вариант 11.
# Слово очищается от символов .,!?;: по краям и переводится в нижний регистр.
# Пустые результаты пропускаются, повторы сохраняются.

text = input("Введите текст: ")

count = 0

for word in text.split():
    cleaned_word = word.strip(".,!?;:").lower()
    if cleaned_word == "":
        continue
    if 3 <= len(cleaned_word) <= 5:
        print(cleaned_word)
        count += 1

if count == 0:
    print("Нет совпадений")

print(f"Количество: {count}")
