# calculator.py — калькулятор с одной операцией
# Лабораторная работа 3, обязательное задание 2.
# eval() не используется: операция выбирается ветвлением.

first = float(input("Первое число: "))
operation = input("Операция (+, -, *, /): ")
second = float(input("Второе число: "))

if operation == "+":
    print(f"Результат: {first + second:.2f}")
elif operation == "-":
    print(f"Результат: {first - second:.2f}")
elif operation == "*":
    print(f"Результат: {first * second:.2f}")
elif operation == "/":
    if second == 0:
        print("Деление на ноль запрещено")
    else:
        print(f"Результат: {first / second:.2f}")
else:
    print("Неизвестная операция")
