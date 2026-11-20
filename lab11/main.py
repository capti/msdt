"""Чтение, анализ и сохранение результатов лабораторной работы 11."""

import json
from pathlib import Path

from analysis import completion_counts, leader_tasks, select_tasks, top_users, validate_todos


def read_positive_integer(input_function=input, output_function=print):
    """Повторяет ввод, пока не получено целое число больше нуля."""
    while True:
        text = input_function("Введите положительный целый user_id: ")
        try:
            number = int(text)
        except ValueError:
            output_function("Нужно ввести целое число")
            continue
        if number <= 0:
            output_function("Число должно быть больше нуля")
            continue
        return number


def read_nonnegative_integer(input_function=input, output_function=print):
    """Повторяет ввод, пока не получено целое число не меньше нуля."""
    while True:
        text = input_function("Введите неотрицательный целый порог: ")
        try:
            number = int(text)
        except ValueError:
            output_function("Нужно ввести целое число")
            continue
        if number < 0:
            output_function("Число должно быть неотрицательным")
            continue
        return number


def process(folder, user_id, threshold):
    """Читает и проверяет вход, затем записывает результаты.

    Возвращает True при успехе и False при любой ожидаемой ошибке.
    При ошибке входа прежние результаты не перезаписываются.
    """
    source = folder / "todos.json"
    leaders_path = folder / "leaders.json"
    selected_path = folder / "selected.json"

    try:
        with open(source, "r", encoding="utf-8") as file:
            data = json.load(file)
        validate_todos(data)
    except FileNotFoundError:
        print(f"Ошибка: файл {source} не найден. Результаты не изменены.")
        return False
    except UnicodeError:
        print(f"Ошибка: неверная кодировка файла {source}. Результаты не изменены.")
        return False
    except json.JSONDecodeError as error:
        print(f"Ошибка JSON: {error}. Результаты не изменены.")
        return False
    except ValueError as error:
        print(f"Ошибка структуры данных: {error}. Результаты не изменены.")
        return False
    except OSError as error:
        print(f"Ошибка доступа: {error}. Результаты не изменены.")
        return False

    counts = completion_counts(data)
    leaders = top_users(counts)
    leaders_data = leader_tasks(data, leaders)
    selected_data = select_tasks(data, user_id, threshold)

    try:
        with open(leaders_path, "w", encoding="utf-8") as file:
            json.dump(leaders_data, file, ensure_ascii=False, indent=2)
        with open(selected_path, "w", encoding="utf-8") as file:
            json.dump(selected_data, file, ensure_ascii=False, indent=2)
    except OSError as error:
        print(f"Ошибка записи: {error}")
        return False

    print("Количества завершённых задач:", counts)
    print("Лидеры:", leaders)
    print("ID задач лидеров:", [item["id"] for item in leaders_data])
    print("Выбранные ID:", [item["id"] for item in selected_data])
    print(f"Результаты сохранены: {leaders_path}, {selected_path}")
    return True


def main():
    folder = Path(__file__).resolve().parent
    user_id = read_positive_integer()
    threshold = read_nonnegative_integer()
    process(folder, user_id, threshold)


if __name__ == "__main__":
    main()
