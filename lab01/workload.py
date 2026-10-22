# workload.py — учебная нагрузка за неделю
# Лабораторная работа 1, обязательное задание 2.

print("Введите данные учебной нагрузки.")

first_subject = input("Название первого предмета: ")
first_lessons = int(input("Занятий первого предмета за неделю: "))
first_minutes = int(input("Минут в одном занятии первого предмета: "))

second_subject = input("Название второго предмета: ")
second_lessons = int(input("Занятий второго предмета за неделю: "))
second_minutes = int(input("Минут в одном занятии второго предмета: "))

first_total_minutes = first_lessons * first_minutes
second_total_minutes = second_lessons * second_minutes
load_minutes = first_total_minutes + second_total_minutes
load_hours = load_minutes / 60

# Суммарная нагрузка уже известна, поэтому минимум показываем в подсказке
# и не просим вводить его повторно.
available_hours = float(
    input(f"Доступно часов в неделю (не меньше {load_hours:.2f}): ")
)

free_hours = available_hours - load_hours
four_weeks_hours = load_hours * 4

print()
print("=" * 48)
print("УЧЕБНАЯ НАГРУЗКА ЗА НЕДЕЛЮ".center(48))
print("=" * 48)
print(f"{first_subject}: {first_lessons} зан. * {first_minutes} мин = "
      f"{first_total_minutes} мин")
print(f"{second_subject}: {second_lessons} зан. * {second_minutes} мин = "
      f"{second_total_minutes} мин")
print("-" * 48)
print(f"{'Общая нагрузка:':<28}{load_minutes} мин")
print(f"{'Общая нагрузка:':<28}{load_hours:.2f} ч")
print(f"{'Доступно за неделю:':<28}{available_hours:.2f} ч")
print(f"{'Свободное время:':<28}{free_hours:.2f} ч")
print(f"{'Нагрузка за 4 недели:':<28}{four_weeks_hours:.2f} ч")
print("=" * 48)
