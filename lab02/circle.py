# circle.py — дополнительное задание: длина окружности и площадь круга
# Радиус положительный, поэтому math.sqrt не нужен, а деления на ноль нет.

import math

radius = float(input("Радиус окружности: "))

circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print(f"Длина окружности: {circumference:.2f}")
print(f"Площадь круга: {area:.2f}")
