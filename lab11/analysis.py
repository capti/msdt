"""Анализ учебного набора задач. Lab 11 (вариант 11)."""


def validate_todos(data):
    """Проверяет структуру набора задач. При нарушении вызывает ValueError.

    Корень — список; каждая запись — словарь с положительными целыми id и
    userId, непустой строкой title и логическим completed. id уникален.
    Дополнительные ключи допустимы.
    """
    if not isinstance(data, list):
        raise ValueError("Корень данных должен быть списком")

    seen_ids = set()
    for index, item in enumerate(data, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"Запись {index}: ожидался словарь")
        for field in ("id", "userId", "title", "completed"):
            if field not in item:
                raise ValueError(f"Запись {index}: отсутствует поле {field}")

        task_id = item["id"]
        if type(task_id) is not int or task_id <= 0:
            raise ValueError(f"Запись {index}: id должен быть положительным целым")

        user_id = item["userId"]
        if type(user_id) is not int or user_id <= 0:
            raise ValueError(f"Запись {index}: userId должен быть положительным целым")

        title = item["title"]
        if not isinstance(title, str) or not title.strip():
            raise ValueError(f"Запись {index}: title должен быть непустой строкой")

        if type(item["completed"]) is not bool:
            raise ValueError(f"Запись {index}: completed должен быть логическим значением")

        if task_id in seen_ids:
            raise ValueError(f"Запись {index}: повторный id {task_id}")
        seen_ids.add(task_id)


def completion_counts(todos):
    """Словарь числа завершённых задач для всех пользователей набора.

    Пользователи с нулём завершённых задач тоже присутствуют в словаре.
    """
    counts = {}
    for item in todos:
        user_id = item["userId"]
        if user_id not in counts:
            counts[user_id] = 0
        if item["completed"]:
            counts[user_id] += 1
    return counts


def top_users(counts):
    """Отсортированный список пользователей с максимальным числом задач.

    Для пустого словаря или максимума 0 возвращает [].
    """
    if not counts:
        return []
    maximum = max(counts.values())
    if maximum == 0:
        return []
    return sorted(user for user, count in counts.items() if count == maximum)


def leader_tasks(todos, leaders):
    """Завершённые задачи лидеров в исходном порядке."""
    result = []
    for item in todos:
        if item["userId"] in leaders and item["completed"]:
            result.append(item)
    return result


def select_tasks(todos, user_id, parameter=None):
    """Вариант 11: завершённые задачи пользователя с id больше порога.

    parameter — целое неотрицательное число (порог). Порядок записей
    сохраняется, исходные записи не изменяются. Для неизвестного
    пользователя результат пуст.
    """
    if parameter is None or type(parameter) is bool:
        raise ValueError("Для варианта 11 нужен целый неотрицательный порог")
    if isinstance(parameter, float) and not parameter.is_integer():
        raise ValueError("Порог должен быть целым числом")
    try:
        threshold = int(parameter)
    except (TypeError, ValueError):
        raise ValueError("Порог должен быть целым неотрицательным числом")
    if threshold < 0:
        raise ValueError("Порог должен быть неотрицательным")

    result = []
    for item in todos:
        if item["userId"] == user_id and item["completed"] and item["id"] > threshold:
            result.append(item)
    return result
