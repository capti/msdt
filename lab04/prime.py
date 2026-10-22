# prime.py — дополнительное задание: проверка простоты числа
# Перебираем делители, пока divisor * divisor <= n, то есть до sqrt(n).

n = int(input("Целое число n >= 2: "))

divisor = 2
is_prime = True

while divisor * divisor <= n:
    if n % divisor == 0:
        is_prime = False
        break
    divisor += 1

if is_prime:
    print("Простое")
else:
    print("Составное")
