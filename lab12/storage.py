"""Чтение и запись JSON для итогового проекта. Без консольных диалогов."""

import json

from logic import validate_records


def load_records(path):
    """Читает и проверяет JSON, возвращает список записей.

    Не изменяет файл. Отсутствующий файл вызывает FileNotFoundError,
    повреждённый JSON — json.JSONDecodeError, неверная структура — ValueError,
    неверная кодировка — UnicodeError, проблемы доступа — OSError.
    """
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return validate_records(data)


def save_records(path, records):
    """Проверяет и записывает список в JSON в UTF-8. Возвращает None.

    При неверной структуре вызывается ValueError до открытия файла,
    при проблеме записи — OSError.
    """
    validate_records(records)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=2)
