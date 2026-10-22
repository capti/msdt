# time_parts.py — перевод секунд в часы, минуты и секунды
# Лабораторная работа 2, обязательное задание 1.
# Часы могут превышать 23: это полное количество часов, а не время суток.

total_seconds = int(input("Общее количество секунд: "))

hours = total_seconds // 3600
minutes = total_seconds % 3600 // 60
seconds = total_seconds % 60

print(f"{hours} ч {minutes} мин {seconds} с")
