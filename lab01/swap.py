# swap.py — обмен значений двух переменных через третью переменную
# Лабораторная работа 1, обязательное задание 4.

first_room = input("Первая аудитория: ")
second_room = input("Вторая аудитория: ")

print()
print(f"Исходные значения: first_room = {first_room}, "
      f"second_room = {second_room}")

# Временная переменная сохраняет первое значение, пока во вторую переменную
# записывается второе, а затем сохранённое значение возвращается обратно.
temporary_room = first_room
first_room = second_room
second_room = temporary_room

print(f"После обмена: first_room = {first_room}, "
      f"second_room = {second_room}")
