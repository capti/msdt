# variant.py — заказ в магазине растений, вариант 11
# Позиции варианта: «Саженцы» и «Горшки».
# Только последовательные команды: без условий, циклов и коллекций.

print("Оформление заказа в магазине растений.")

order_title = input("Название заказа: ")
customer_name = input("Имя заказчика: ")

first_name = input("Название первой позиции: ")
first_quantity = int(input("Количество первой позиции: "))
first_price = float(input("Цена первой позиции, руб.: "))

second_name = input("Название второй позиции: ")
second_quantity = int(input("Количество второй позиции: "))
second_price = float(input("Цена второй позиции, руб.: "))

first_cost = first_quantity * first_price
second_cost = second_quantity * second_price
goods_total = first_cost + second_cost

delivery_cost = float(input("Стоимость доставки, руб.: "))
total = goods_total + delivery_cost

paid = float(input(f"Внесённая сумма, руб. (не меньше {total:.2f}): "))

total_quantity = first_quantity + second_quantity
change = paid - total

line = "-" * 60

print()
print("=" * 60)
print(order_title.center(60))
print("=" * 60)
print(f"Заказчик: {customer_name}")
print(line)
print(f"{'Товар':<24}{'Кол-во':>8}{'Цена':>12}{'Стоимость':>16}")
print(line)
print(f"{first_name:<24}{first_quantity:>8}{first_price:>12.2f}"
      f"{first_cost:>16.2f}")
print(f"{second_name:<24}{second_quantity:>8}{second_price:>12.2f}"
      f"{second_cost:>16.2f}")
print(line)
print(f"{'Стоимость товаров без доставки:':<44}{goods_total:>16.2f}")
print(f"{'Доставка:':<44}{delivery_cost:>16.2f}")
print(f"{'Итого с доставкой:':<44}{total:>16.2f}")
print(f"{'Всего единиц товара:':<44}{total_quantity:>16}")
print(f"{'Внесено:':<44}{paid:>16.2f}")
print(f"{'Сдача:':<44}{change:>16.2f}")
print("=" * 60)
