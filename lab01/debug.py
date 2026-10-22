# debug.py — исправление трёх независимых фрагментов
# Лабораторная работа 1, обязательное задание 3.
#
# Ошибочный код и причины ошибок:
#   А. first = "2"; second = "3"; print(first + second)  -> "23", потому что
#      строки склеиваются, а нужна сумма чисел.
#   Б. age = input(...); print(age + 1)                  -> TypeError, потому что
#      input() возвращает str, а str и int складывать нельзя.
#   В. average = first + second + third / 3             -> 14.333..., потому что
#      сначала выполняется деление third / 3, а не деление суммы.

# --- Фрагмент А: сумма чисел ---

first_text = "2"
second_text = "3"

print("А. Значения до преобразования:")
print(f"   first_text = {first_text!r}, тип: {type(first_text).__name__}")
print(f"   second_text = {second_text!r}, тип: {type(second_text).__name__}")
print(f"   first_text + second_text = {first_text + second_text!r} "
      f"(склеивание строк)")

first = int(first_text)
second = int(second_text)

print("А. Значения после преобразования:")
print(f"   first = {first}, тип: {type(first).__name__}")
print(f"   second = {second}, тип: {type(second).__name__}")
print(f"А. Сумма чисел: {first + second}")

# --- Фрагмент Б: возраст через год ---

age_text = input("Б. Возраст: ")
print(f"   age_text = {age_text!r}, тип: {type(age_text).__name__}")

age = int(age_text)
print(f"   age = {age}, тип: {type(age).__name__}")
print(f"Б. Возраст через год: {age + 1}")

# --- Фрагмент В: среднее трёх чисел ---

third_first = 4
third_second = 7
third_third = 10

# Скобки меняют порядок вычислений: сначала сумма, затем деление.
average = (third_first + third_second + third_third) / 3

print(f"В. Среднее чисел {third_first}, {third_second}, {third_third}: {average}")
