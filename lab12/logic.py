"""Логика итогового проекта: план посадки растений. Lab 12 (вариант 11)."""


def validate_records(records):
    """Проверяет набор записей и возвращает его. При ошибке — ValueError.

    Не изменяет записи. Каждая запись — словарь с обязательными ключами
    id, title, category, amount, completed:

    - id — положительное уникальное целое (логическое значение не подходит);
    - title, category — непустые после strip() строки;
    - amount — целое не меньше нуля (логическое значение не подходит);
    - completed — строго bool.

    Дополнительные ключи допустимы и не проверяются.
    """
    if not isinstance(records, list):
        raise ValueError("Корень данных должен быть списком")

    seen_ids = set()
    for index, record in enumerate(records, start=1):
        if not isinstance(record, dict):
            raise ValueError(f"Запись {index}: ожидался словарь")
        for field in ("id", "title", "category", "amount", "completed"):
            if field not in record:
                raise ValueError(f"Запись {index}: отсутствует поле {field}")

        record_id = record["id"]
        if type(record_id) is not int or record_id <= 0:
            raise ValueError(f"Запись {index}: id должен быть положительным целым")
        if record_id in seen_ids:
            raise ValueError(f"Запись {index}: повторный id {record_id}")
        seen_ids.add(record_id)

        title = record["title"]
        if not isinstance(title, str) or not title.strip():
            raise ValueError(f"Запись {index}: title должен быть непустой строкой")
        category = record["category"]
        if not isinstance(category, str) or not category.strip():
            raise ValueError(f"Запись {index}: category должна быть непустой строкой")

        amount = record["amount"]
        if type(amount) is not int or amount < 0:
            raise ValueError(f"Запись {index}: amount должен быть целым не меньше нуля")
        if type(record["completed"]) is not bool:
            raise ValueError(f"Запись {index}: completed должен быть логическим значением")
    return records


def add_record(records, title, category, amount):
    """Добавляет запись и возвращает её. Изменяет records.

    Краевые пробелы в title и category убираются. Новый id равен
    максимальному существующему плюс 1; для пустого списка — 1.
    Начальный статус False. Идентификаторы существующих записей не меняются.
    Некорректные значения вызывают ValueError.
    """
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Название должно быть непустой строкой")
    if not isinstance(category, str) or not category.strip():
        raise ValueError("Категория должна быть непустой строкой")
    if type(amount) is not int or amount < 0:
        raise ValueError("Количество должно быть целым не меньше нуля")

    record_id = max((item["id"] for item in records), default=0) + 1
    record = {
        "id": record_id,
        "title": title.strip(),
        "category": category.strip(),
        "amount": amount,
        "completed": False,
    }
    records.append(record)
    return record


def find_records(records, query):
    """Возвращает записи, название которых содержит query без учёта регистра.

    Не изменяет records. Пустой запрос вызывает ValueError.
    """
    if not isinstance(query, str) or not query.strip():
        raise ValueError("Поисковый запрос не должен быть пустым")
    needle = query.strip().lower()
    return [item for item in records if needle in item["title"].lower()]


def set_completed(records, record_id, completed):
    """Явно устанавливает статус. Возвращает True при успехе, False если ID не найден.

    Изменяет records только при найденной записи. completed должен быть bool.
    """
    if type(completed) is not bool:
        raise ValueError("completed должен быть логическим значением")
    for record in records:
        if record["id"] == record_id:
            record["completed"] = completed
            return True
    return False


def delete_record(records, record_id):
    """Удаляет запись по ID. Возвращает True при успехе, False если ID не найден.

    Изменяет records только при найденной записи; остальные ID не меняются.
    """
    for index, record in enumerate(records):
        if record["id"] == record_id:
            del records[index]
            return True
    return False


def statistics(records):
    """Возвращает сводку. Не изменяет records.

    Ключи результата: total, completed, pending, amount_total, by_category.
    Категории сравниваются точно после удаления краевых пробелов и выводятся
    в алфавитном порядке. Для пустого списка все значения равны 0.
    """
    by_category = {}
    completed = 0
    amount_total = 0
    for record in records:
        amount_total += record["amount"]
        if record["completed"]:
            completed += 1
        category = record["category"].strip()
        by_category[category] = by_category.get(category, 0) + record["amount"]
    return {
        "total": len(records),
        "completed": completed,
        "pending": len(records) - completed,
        "amount_total": amount_total,
        "by_category": {key: by_category[key] for key in sorted(by_category)},
    }
