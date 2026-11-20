"""Проверки логики итогового проекта: python test_logic.py"""

from logic import (
    add_record,
    delete_record,
    find_records,
    set_completed,
    statistics,
    validate_records,
)

SAMPLE = [
    {"id": 1, "title": "Томаты", "category": "овощи", "amount": 4, "completed": False},
    {"id": 2, "title": "Базилик", "category": "зелень", "amount": 2, "completed": True},
    {"id": 3, "title": "Петуния", "category": "цветы", "amount": 6, "completed": True},
    {"id": 4, "title": "Огурцы", "category": "овощи", "amount": 3, "completed": False},
]


def make(record_id=1, title="Растение", category="овощи", amount=1, completed=False, **extra):
    record = {
        "id": record_id,
        "title": title,
        "category": category,
        "amount": amount,
        "completed": completed,
    }
    record.update(extra)
    return record


def check_value_error(action):
    try:
        action()
    except ValueError:
        pass
    else:
        assert False, "Ошибка не обнаружена"


# Проверка структуры
assert validate_records(SAMPLE) == SAMPLE
validate_records([make(title="О одинаковое"), make(record_id=2, title="Одинаковое")])
validate_records([make(note="дополнительный ключ")])
print("Проверка структуры пройдена")

# Неверные структуры и строгие типы
check_value_error(lambda: validate_records({"id": 1}))
check_value_error(lambda: validate_records(["строка"]))
check_value_error(lambda: validate_records([{"id": 1, "title": "A", "category": "B", "amount": 1}]))
check_value_error(lambda: validate_records([make(record_id=True)]))
check_value_error(lambda: validate_records([make(record_id=0)]))
check_value_error(lambda: validate_records([make(title="   ")]))
check_value_error(lambda: validate_records([make(category=5)]))
check_value_error(lambda: validate_records([make(amount=True)]))
check_value_error(lambda: validate_records([make(amount=-1)]))
check_value_error(lambda: validate_records([make(completed="false")]))
check_value_error(lambda: validate_records([make(), make()]))
print("Проверка неверных структур пройдена")

# Добавление: пустой список, обрезка пробелов, новый ID, исходные ID не меняются
empty = []
added = add_record(empty, "  Мята  ", "  зелень  ", 5)
assert empty == [make(record_id=1, title="Мята", category="зелень", amount=5)]
assert added["completed"] is False
records = [make(record_id=1), make(record_id=2)]
assert add_record(records, "Шалфей", "зелень", 1)["id"] == 3
remaining = [make(record_id=1), make(record_id=2)]
del remaining[0]
assert add_record(remaining, "Петрушка", "зелень", 1)["id"] == 3
check_value_error(lambda: add_record([], "", "зелень", 1))
check_value_error(lambda: add_record([], "Мята", "  ", 1))
check_value_error(lambda: add_record([], "Мята", "зелень", -1))
check_value_error(lambda: add_record([], "Мята", "зелень", True))
print("Проверка добавления пройдена")

# Поиск без учёта регистра, пустой запрос, нет совпадений, исходные данные не меняются
assert [item["id"] for item in find_records(SAMPLE, "том")] == [1]
assert [item["id"] for item in find_records(SAMPLE, "ОГУРЦЫ")] == [4]
assert [item["id"] for item in find_records(SAMPLE, "  Петуния  ")] == [3]
assert find_records(SAMPLE, "несуществующее") == []
check_value_error(lambda: find_records(SAMPLE, "  "))
assert len(SAMPLE) == 4
print("Проверка поиска пройдена")

# Изменение статуса: явная установка, неизвестный ID
records = [make(record_id=1), make(record_id=2, completed=True)]
assert set_completed(records, 2, False) is True
assert records[1]["completed"] is False
assert set_completed(records, 1, True) is True
assert records[0]["completed"] is True
assert set_completed(records, 99, True) is False
assert [item["completed"] for item in records] == [True, False]
check_value_error(lambda: set_completed(records, 1, "true"))
print("Проверка статуса пройдена")

# Удаление: известный и неизвестный ID, остальные ID сохраняются
records = [make(record_id=1), make(record_id=2)]
assert delete_record(records, 1) is True
assert [item["id"] for item in records] == [2]
assert delete_record(records, 99) is False
assert [item["id"] for item in records] == [2]
print("Проверка удаления пройдена")

# Статистика: учебный набор, пустой список, две категории, обрезка категорий
stats = statistics(SAMPLE)
assert stats["total"] == 4
assert stats["completed"] == 2
assert stats["pending"] == 2
assert stats["amount_total"] == 15
assert stats["by_category"] == {"зелень": 2, "овощи": 7, "цветы": 6}
assert list(stats["by_category"]) == ["зелень", "овощи", "цветы"]

empty_stats = statistics([])
assert empty_stats == {
    "total": 0,
    "completed": 0,
    "pending": 0,
    "amount_total": 0,
    "by_category": {},
}
pair = [make(record_id=1, amount=4), make(record_id=2, amount=2, completed=True)]
pair_stats = statistics(pair)
assert (pair_stats["total"], pair_stats["completed"],
        pair_stats["pending"], pair_stats["amount_total"]) == (2, 1, 1, 6)
two = [make(record_id=1, category=" овощи ", amount=3),
       make(record_id=2, category="овощи", amount=2),
       make(record_id=3, category="цветы", amount=1, completed=True)]
validate_records(two)
assert statistics(two)["by_category"] == {"овощи": 5, "цветы": 1}
assert statistics(two)["amount_total"] == 6
assert len(SAMPLE) == 4
print("Проверка статистики пройдена")

print("Все проверки логики пройдены")
