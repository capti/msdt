"""Проверки лабораторной работы 11: python test_analysis.py"""

import json
from pathlib import Path
from tempfile import TemporaryDirectory

from analysis import (
    completion_counts,
    leader_tasks,
    select_tasks,
    top_users,
    validate_todos,
)
from main import process

DEMO = [
    {"id": 1, "userId": 5, "title": "Ввод", "completed": True},
    {"id": 2, "userId": 5, "title": "Циклы", "completed": False},
    {"id": 3, "userId": 10, "title": "Строки", "completed": True},
    {"id": 4, "userId": 10, "title": "Файлы", "completed": True},
    {"id": 5, "userId": 5, "title": "Списки", "completed": True},
]
DEMO_COPY = [row.copy() for row in DEMO]


def check_value_error(action):
    """Проверяет, что действие вызывает ValueError."""
    try:
        action()
    except ValueError:
        pass
    else:
        assert False, "Ошибка не обнаружена"


# Учебный набор: проверка структуры, количества, лидеры, задачи лидеров
validate_todos(DEMO)
assert completion_counts(DEMO) == {5: 2, 10: 2}
assert top_users(completion_counts(DEMO)) == [5, 10]
assert [item["id"] for item in leader_tasks(DEMO, [5, 10])] == [1, 3, 4, 5]
print("Проверка учебного набора пройдена")

# Пустой список
assert completion_counts([]) == {}
assert top_users({}) == []
assert leader_tasks([], []) == []
assert select_tasks([], 5, 2) == []
print("Проверка пустого набора пройдена")

# Набор только с completed=false
pending = [
    {"id": 1, "userId": 5, "title": "A", "completed": False},
    {"id": 2, "userId": 10, "title": "B", "completed": False},
]
validate_todos(pending)
assert completion_counts(pending) == {5: 0, 10: 0}
assert top_users(completion_counts(pending)) == []
assert leader_tasks(pending, []) == []
assert select_tasks(pending, 5, 0) == []
print("Проверка набора без завершённых задач пройдена")

# Один лидер и несколько лидеров с одинаковым результатом
single = [
    {"id": 1, "userId": 1, "title": "A", "completed": True},
    {"id": 2, "userId": 2, "title": "B", "completed": False},
]
validate_todos(single)
assert top_users(completion_counts(single)) == [1]
assert top_users({3: 1, 7: 1, 4: 0}) == [3, 7]
print("Проверка лидеров пройдена")

# Индивидуальный вариант 11: завершённые с id больше порога
assert [item["id"] for item in select_tasks(DEMO, 5, 2)] == [5]
assert [item["id"] for item in select_tasks(DEMO, 5, "2")] == [5]
assert [item["id"] for item in select_tasks(DEMO, 10, 2)] == [3, 4]
assert select_tasks(DEMO, 99, 2) == []
assert select_tasks(DEMO, 5, 100) == []
# равенство границе: id == порог не включается
assert [item["id"] for item in select_tasks(DEMO, 5, 1)] == [5]
assert [item["id"] for item in select_tasks(DEMO, 10, 3)] == [4]
assert select_tasks(DEMO, 5, 5) == []
check_value_error(lambda: select_tasks(DEMO, 5, -1))
check_value_error(lambda: select_tasks(DEMO, 5, None))
print("Проверка варианта 11 пройдена")

# Дополнительные ключи допустимы
validate_todos([{"id": 9, "userId": 7, "title": "X", "completed": False, "note": "ок"}])

# Неверные структуры
check_value_error(lambda: validate_todos({"id": 1}))
check_value_error(lambda: validate_todos([DEMO[0], DEMO[0].copy()]))
check_value_error(lambda: validate_todos([{"id": 1, "title": "A", "completed": True}]))
check_value_error(lambda: validate_todos([
    {"id": 1, "userId": 5, "title": "A", "completed": "false"},
]))
check_value_error(lambda: validate_todos([
    {"id": True, "userId": 5, "title": "A", "completed": True},
]))
check_value_error(lambda: validate_todos([
    {"id": 1, "userId": 5, "title": "   ", "completed": True},
]))
check_value_error(lambda: validate_todos([
    {"id": 1, "userId": 5, "title": "A", "completed": 1},
]))
print("Проверки неверной структуры пройдены")

# Исходные записи не изменяются
assert DEMO == DEMO_COPY

# Запись и повторное чтение JSON
with TemporaryDirectory() as directory:
    path = Path(directory) / "selected.json"
    selected = select_tasks(DEMO, 5, 2)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(selected, file, ensure_ascii=False, indent=2)
    with open(path, "r", encoding="utf-8") as file:
        restored = json.load(file)
    assert restored == selected
    text = path.read_text(encoding="utf-8")
    assert '"title": "Списки"' in text
print("Проверка записи JSON пройдена")

# Сохранность прежних результатов при неверном входе
with TemporaryDirectory() as directory:
    folder = Path(directory)
    (folder / "todos.json").write_text(
        json.dumps(DEMO, ensure_ascii=False), encoding="utf-8"
    )
    assert process(folder, 5, 2) is True
    leaders_path = folder / "leaders.json"
    original = leaders_path.read_text(encoding="utf-8")
    assert [item["id"] for item in json.loads(original)] == [1, 3, 4, 5]

    (folder / "todos.json").write_text('{"id": 1}', encoding="utf-8")
    assert process(folder, 5, 2) is False
    assert leaders_path.read_text(encoding="utf-8") == original
print("Проверка сохранности результатов пройдена")

print("Все проверки пройдены")
