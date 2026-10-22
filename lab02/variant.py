# variant.py — вариант 11: страницы и тетради
# Лабораторная работа 2, вариант 11.
# total_pages — общий объём (страницы), pages_per_notebook — вместимость
# одной единицы (страниц в тетради).
# Циклы и условия не используются: число тетрадей считается формулой ceil.

total_pages = int(input("Количество страниц: "))
pages_per_notebook = int(input("Страниц в тетради: "))

full_notebooks = total_pages // pages_per_notebook
remaining_pages = total_pages % pages_per_notebook
notebooks_needed = (total_pages + pages_per_notebook - 1) // pages_per_notebook

print(f"Полных тетрадей: {full_notebooks}")
print(f"Остаток страниц: {remaining_pages}")
print(f"Всего тетрадей нужно: {notebooks_needed}")
