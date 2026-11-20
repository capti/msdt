"""Консольный интерфейс итогового проекта. Lab 12 (вариант 11)."""

import json
from pathlib import Path

from logic import add_record, delete_record, find_records, set_completed, statistics
from storage import load_records, save_records


def by_id(record):
    """Ключ сортировки записей по идентификатору."""
    return record["id"]


def format_record(record):
    """Одна строка списка: ID, название, категория, количество, статус."""
    status = "посадка выполнена" if record["completed"] else "посадка не выполнена"
    return (
        f"{record['id']} | {record['title']} | {record['category']} | "
        f"{record['amount']} раст. | {status}"
    )


def read_text(prompt):
    """Запрашивает непустую строку, убирая краевые пробелы."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Значение не должно быть пустым")


def read_amount():
    """Запрашивает целое количество растений не меньше нуля."""
    while True:
        text = input("Количество растений: ").strip()
        try:
            amount = int(text)
        except ValueError:
            print("Нужно ввести целое число")
            continue
        if amount < 0:
            print("Количество должно быть не меньше нуля")
            continue
        return amount


def read_id(prompt):
    """Запрашивает положительный целый идентификатор."""
    while True:
        text = input(prompt).strip()
        try:
            record_id = int(text)
        except ValueError:
            print("Нужно ввести целое число")
            continue
        if record_id <= 0:
            print("ID должен быть положительным")
            continue
        return record_id


def read_yes_no(prompt):
    """Запрашивает ответ «да» или «нет» без учёта регистра."""
    while True:
        answer = input(prompt).strip().lower()
        if answer == "да":
            return True
        if answer == "нет":
            return False
        print("Нужно ответить да или нет")


def read_completed():
    """Явно выбирает новое значение статуса."""
    while True:
        print("1 - посадка выполнена")
        print("2 - посадка не выполнена")
        answer = input("Выберите 1 или 2: ").strip()
        if answer == "1":
            return True
        if answer == "2":
            return False
        print("Нужно ввести 1 или 2")


def save_data(records, path):
    """Сохраняет данные, печатает об успехе только после записи."""
    try:
        save_records(path, records)
    except OSError as error:
        print(f"Ошибка сохранения: {error}")
        return False
    except ValueError as error:
        print(f"Ошибка данных при сохранении: {error}")
        return False
    print(f"Данные сохранены: {path}")
    return True


def load_on_start(path):
    """Загружает данные при запуске. Возвращает None при ошибке загрузки."""
    if not path.exists():
        print(f"Файл {path} не найден — начинаем с пустого списка.")
        return []
    try:
        return load_records(path)
    except (UnicodeError, json.JSONDecodeError, ValueError, OSError) as error:
        print(f"Ошибка загрузки {path}: {error}")
        print("Запуск прекращён, файл не изменён.")
        return None


def show_menu():
    print()
    print("1 - Показать записи")
    print("2 - Добавить запись")
    print("3 - Найти записи")
    print("4 - Изменить статус")
    print("5 - Удалить запись")
    print("6 - Показать статистику")
    print("7 - Сохранить данные")
    print("8 - Выйти")


def show_records(records):
    if not records:
        print("Нет записей")
        return
    for record in sorted(records, key=by_id):
        print(format_record(record))


def handle_add(records):
    title = read_text("Название растения: ")
    category = read_text("Категория: ")
    amount = read_amount()
    record = add_record(records, title, category, amount)
    print(f"Добавлена запись ID {record['id']}")


def handle_find(records):
    query = read_text("Часть названия: ")
    try:
        found = find_records(records, query)
    except ValueError as error:
        print(error)
        return
    if not found:
        print("Ничего не найдено")
        return
    print(f"Найдено записей: {len(found)}")
    for record in sorted(found, key=by_id):
        print(format_record(record))


def handle_status(records):
    record_id = read_id("ID записи: ")
    completed = read_completed()
    if set_completed(records, record_id, completed):
        print("Статус обновлён")
    else:
        print("Запись с таким ID не найдена")


def handle_delete(records):
    record_id = read_id("ID записи для удаления: ")
    target = None
    for record in records:
        if record["id"] == record_id:
            target = record
            break
    if target is None:
        print("Запись с таким ID не найдена")
        return
    print("Найдена:", format_record(target))
    if read_yes_no("Удалить? да/нет: "):
        delete_record(records, record_id)
        print("Запись удалена")
    else:
        print("Удаление отменено")


def show_statistics(records):
    stats = statistics(records)
    print("Всего записей:", stats["total"])
    print("Выполнено:", stats["completed"])
    print("Не выполнено:", stats["pending"])
    print("Всего растений:", stats["amount_total"], "раст.")
    print("По категориям:")
    if stats["by_category"]:
        for category, amount in stats["by_category"].items():
            print(f"  {category}: {amount} раст.")
    else:
        print("  Нет категорий")


def handle_exit(records, path):
    """Возвращает True, если можно завершить программу."""
    while True:
        answer = input("Сохранить данные перед выходом? да/нет: ").strip().lower()
        if answer == "нет":
            print("Выход без сохранения.")
            return True
        if answer == "да":
            if save_data(records, path):
                return True
            print("Сохранение не удалось — возврат в меню.")
            return False
        print("Нужно ответить да или нет")


def main():
    path = Path(__file__).resolve().parent / "data.json"
    records = load_on_start(path)
    if records is None:
        return

    while True:
        show_menu()
        command = input("Команда: ").strip()
        if command == "1":
            show_records(records)
        elif command == "2":
            handle_add(records)
        elif command == "3":
            handle_find(records)
        elif command == "4":
            handle_status(records)
        elif command == "5":
            handle_delete(records)
        elif command == "6":
            show_statistics(records)
        elif command == "7":
            save_data(records, path)
        elif command == "8":
            if handle_exit(records, path):
                break
        else:
            print("Неизвестная команда. Повторите ввод.")


if __name__ == "__main__":
    main()
