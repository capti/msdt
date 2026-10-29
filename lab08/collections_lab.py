"""Лабораторная работа 8: словари, множества и кортежи.

Обязательные задания 1-2, индивидуальный вариант 11
(«Коллекция растений», поле amount — количество растений)
и дополнительное задание — сортировка сводки по убыванию суммы.
"""

PUNCTUATION = ".,!?;:"

RECORDS = [
    {"title": "Монстера", "category": "комнатные", "amount": 3},
    {"title": "Кактус опунция", "category": "суккуленты", "amount": 5},
    {"title": "Тюльпан", "category": "уличные", "amount": 12},
    {"title": "Фикус", "category": "комнатные", "amount": 2},
    {"title": "Алоэ", "category": "суккуленты", "amount": 4},
    {"title": "Роза кустовая", "category": "уличные", "amount": 6},
]


def word_counts(text):
    """Словарь «слово -> количество» для текста в нижнем регистре."""
    counts = {}
    for piece in text.lower().split():
        word = piece.strip(PUNCTUATION)
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts


def print_word_counts(text):
    """Печать пар «слово: количество» по алфавиту."""
    counts = word_counts(text)
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")


def common_topics(first, second):
    """Отсортированный список общих тем (пересечение множеств)."""
    return sorted(set(first) & set(second))


def all_topics(first, second):
    """Отсортированный список всех уникальных тем (объединение множеств)."""
    return sorted(set(first) | set(second))


def make_record():
    """Запись «title, hours» с изменением hours и добавлением completed."""
    record = {"title": "Python", "hours": 4}
    record["hours"] = 6
    record["completed"] = False
    return record


def make_pair(record):
    """Кортеж (title, hours), собранный из записи."""
    return (record["title"], record["hours"])


def totals_by_category(records):
    """Словарь «категория -> сумма amount» без изменения входных записей."""
    totals = {}
    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0) + record["amount"]
    return totals


def titles_in_category(records, category):
    """Названия записей указанной категории в исходном порядке."""
    titles = []
    for record in records:
        if record["category"] == category:
            titles.append(record["title"])
    return titles


def sorted_totals(records):
    """Список пар (категория, сумма) по убыванию суммы, затем по алфавиту."""
    totals = totals_by_category(records)
    return sorted(totals.items(), key=lambda item: (-item[1], item[0]))


def main():
    """Интерактивный запуск: сводка по категориям и поиск по введённой."""
    record = make_record()
    title, hours = make_pair(record)
    print(f"Запись: {record}")
    print(f"Пара: {title}, {hours}")
    print()

    print("Слова:")
    print_word_counts("Python, python! SQL sql sql git")
    print()

    print("Темы:", common_topics(["python", "sql", "python"], ["sql", "git"]))
    print("Все темы:", all_topics(["python", "sql", "python"], ["sql", "git"]))
    print()

    print("Сводка по категориям (по алфавиту):")
    totals = totals_by_category(RECORDS)
    for category in sorted(totals):
        print(f"{category}: {totals[category]}")
    print()

    print("Сводка по убыванию суммы:", sorted_totals(RECORDS))
    print()

    category = input("Категория для поиска: ").strip()
    print(titles_in_category(RECORDS, category))


if __name__ == "__main__":
    main()
