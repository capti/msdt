"""Управляемое упражнение: получение профиля GitHub. Lab 11.

Сетевой запрос выполняется только по вызову из main(), при импорте
модуля никаких обращений к сети нет.
"""

import json
import socket
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


def check_profile(data):
    """Проверяет, что ответ похож на профиль пользователя."""
    if not isinstance(data, dict) or not isinstance(data.get("login"), str):
        raise ValueError("Ответ не похож на профиль пользователя")


def fetch_profile(login):
    """Получает профиль пользователя GitHub по логину через GET-запрос."""
    if not login.strip():
        raise ValueError("Логин не должен быть пустым")
    url = "https://api.github.com/users/" + quote(login.strip(), safe="")
    request = Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "python-course-lab11",
    })
    with urlopen(request, timeout=10) as response:
        data = json.loads(response.read().decode("utf-8"))
    check_profile(data)
    return data


def choose_source():
    """Меню источника профиля: сеть или локальный учебный пример."""
    print("Источник профиля:")
    print("1 - сеть (GitHub API)")
    print("2 - локальный пример (profile_sample.json)")
    while True:
        choice = input("Выберите 1 или 2: ").strip()
        if choice in ("1", "2"):
            return choice
        print("Нужно ввести 1 или 2")


def show_profile(data):
    """Общая функция вывода профиля для обоих источников."""
    print(f"Логин: {data['login']}")
    print(f"Имя: {data.get('name')}")


def main():
    folder = Path(__file__).resolve().parent
    try:
        source = choose_source()
        if source == "1":
            data = fetch_profile(input("Логин GitHub: "))
            output = folder / "profile.json"
            with open(output, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            print(f"Профиль сохранён: {output}")
        else:
            with open(folder / "profile_sample.json", "r", encoding="utf-8") as file:
                data = json.load(file)
            print("Использованы учебные локальные данные")
        check_profile(data)
        show_profile(data)
    except HTTPError as error:
        print(f"Сервер вернул HTTP {error.code}")
    except (URLError, TimeoutError, socket.timeout):
        print("Не удалось получить ответ по сети")
    except (ValueError, UnicodeError) as error:
        print(f"Ошибка данных: {error}")
    except OSError as error:
        print(f"Ошибка доступа: {error}")


if __name__ == "__main__":
    main()
