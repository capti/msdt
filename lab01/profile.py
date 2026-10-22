# profile.py — карточка студента
# Лабораторная работа 1, обязательное задание 1.
# Все данные запрашиваются заранее, карточка печатается после завершения ввода.

print("Введите данные студента.")

surname = input("Фамилия: ")
name = input("Имя: ")
group = input("Группа: ")
city = input("Город: ")
age = int(input("Возраст в полных годах (1-120): "))
subject = input("Любимый предмет: ")
study_hours = float(input("Часов подготовки в неделю: "))

# Вычисляемые показатели получаем только из введённых данных.
age_in_four_years = age + 4
hours_in_four_weeks = study_hours * 4
hours_per_day = study_hours / 7

line = "=" * 48

print()
print(line)
print("КАРТОЧКА СТУДЕНТА".center(48))
print(line)
print(f"{'Фамилия:':<24}{surname}")
print(f"{'Имя:':<24}{name}")
print(f"{'Группа:':<24}{group}")
print(f"{'Город:':<24}{city}")
print(f"{'Возраст:':<24}{age}")
print(f"{'Любимый предмет:':<24}{subject}")
print(f"{'Подготовка:':<24}{study_hours:.2f} ч в неделю")
print("-" * 48)
print(f"{'Полное имя:':<24}{name} {surname}")
print(f"{'Возраст через 4 года:':<24}{age_in_four_years}")
print(f"{'Подготовка за 4 недели:':<24}{hours_in_four_weeks:.2f} ч")
print(f"{'В среднем в день:':<24}{hours_per_day:.2f} ч")
print(line)
