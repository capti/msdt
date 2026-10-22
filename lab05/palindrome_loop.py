# palindrome_loop.py — дополнительное задание: палиндром без обратного среза
# Сравниваем символы с начала и с конца, обходя половину очищенной строки.

text = input("Введите текст: ")

cleaned = text.replace(" ", "").lower()

if cleaned == "":
    print("Нет текста")
else:
    is_palindrome = True
    for index in range(len(cleaned) // 2):
        if cleaned[index] != cleaned[-1 - index]:
            is_palindrome = False
            break
    if is_palindrome:
        print("Палиндром")
    else:
        print("Не палиндром")
