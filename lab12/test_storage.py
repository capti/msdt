"""Проверки хранения итогового проекта: python test_storage.py"""

import json
from pathlib import Path
from tempfile import TemporaryDirectory

from storage import load_records, save_records

SAMPLE = [
    {"id": 1, "title": "Томаты", "category": "овощи", "amount": 4, "completed": False},
    {"id": 2, "title": "Базилик", "category": "зелень", "amount": 2, "completed": True},
]


# Запись, повторное чтение, читаемая кириллица
with TemporaryDirectory() as directory:
    path = Path(directory) / "data.json"
    save_records(path, SAMPLE)
    assert path.exists()
    assert load_records(path) == SAMPLE
    text = path.read_text(encoding="utf-8")
    assert '"title": "Томаты"' in text
print("Проверка записи и чтения пройдена")

# Отсутствующий файл
with TemporaryDirectory() as directory:
    path = Path(directory) / "missing.json"
    try:
        load_records(path)
    except FileNotFoundError:
        pass
    else:
        assert False, "Ошибка не обнаружена"
print("Проверка отсутствующего файла пройдена")

# Пустой JSON загружается как пустой список
with TemporaryDirectory() as directory:
    path = Path(directory) / "data.json"
    path.write_text("[]", encoding="utf-8")
    assert load_records(path) == []
print("Проверка пустого файла пройдена")

# Повреждённый JSON: файл не изменён
with TemporaryDirectory() as directory:
    path = Path(directory) / "data.json"
    path.write_text('[{"id": 1', encoding="utf-8")
    original = path.read_bytes()
    try:
        load_records(path)
    except json.JSONDecodeError:
        pass
    else:
        assert False, "Ошибка не обнаружена"
    assert path.read_bytes() == original
print("Проверка повреждённого JSON пройдена")

# Неверная структура: файл не изменён
with TemporaryDirectory() as directory:
    path = Path(directory) / "data.json"
    path.write_text(
        '[{"id": 1, "title": "A", "category": "B", "amount": 1, "completed": false},'
        '{"id": 1, "title": "B", "category": "B", "amount": 1, "completed": false}]',
        encoding="utf-8",
    )
    original = path.read_bytes()
    try:
        load_records(path)
    except ValueError as error:
        assert "повторный id" in str(error)
    else:
        assert False, "Ошибка не обнаружена"
    assert path.read_bytes() == original
print("Проверка неверной структуры пройдена")

# Сохранение неверных данных не создаёт файл
with TemporaryDirectory() as directory:
    path = Path(directory) / "data.json"
    bad = [{"id": True, "title": "A", "category": "B", "amount": 1, "completed": False}]
    try:
        save_records(path, bad)
    except ValueError:
        pass
    else:
        assert False, "Ошибка не обнаружена"
    assert not path.exists()
print("Проверка неверных данных при сохранении пройдена")

print("Все проверки хранения пройдены")
