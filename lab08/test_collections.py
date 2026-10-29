"""Проверки для collections_lab.py (лабораторная работа 8).

Запуск: python test_collections.py
"""

from collections_lab import (
    RECORDS,
    all_topics,
    common_topics,
    make_pair,
    make_record,
    sorted_totals,
    titles_in_category,
    totals_by_category,
    word_counts,
)


def test_word_counts_basic():
    assert word_counts("Python, python! SQL") == {"python": 2, "sql": 1}


def test_word_counts_punctuation_only():
    assert word_counts("!!!") == {}


def test_word_counts_empty():
    assert word_counts("") == {}


def test_word_counts_mixed_punctuation():
    assert word_counts("Мяу: мяу, лай. лай!") == {"мяу": 2, "лай": 2}


def test_common_topics():
    first = ["python", "sql", "python"]
    second = ["sql", "git"]
    assert common_topics(first, second) == ["sql"]


def test_all_topics():
    first = ["python", "sql", "python"]
    second = ["sql", "git"]
    assert all_topics(first, second) == ["git", "python", "sql"]


def test_topics_with_empty_list():
    assert common_topics([], ["sql", "git"]) == []
    assert common_topics(["python"], []) == []
    assert all_topics([], ["sql", "git"]) == ["git", "sql"]
    assert all_topics(["python"], []) == ["python"]


def test_record_and_pair():
    record = make_record()
    assert record == {"title": "Python", "hours": 6, "completed": False}
    title, hours = make_pair(record)
    assert title == "Python"
    assert hours == 6


def test_totals_example():
    records = [
        {"title": "A", "category": "основное", "amount": 4},
        {"title": "B", "category": "дополнительное", "amount": 2},
        {"title": "C", "category": "основное", "amount": 3},
    ]
    assert totals_by_category(records) == {"основное": 7, "дополнительное": 2}


def test_titles_example():
    records = [
        {"title": "A", "category": "основное", "amount": 4},
        {"title": "B", "category": "дополнительное", "amount": 2},
        {"title": "C", "category": "основное", "amount": 3},
    ]
    assert titles_in_category(records, "основное") == ["A", "C"]
    assert titles_in_category(records, "нет") == []


def test_totals_empty():
    assert totals_by_category([]) == {}
    assert titles_in_category([], "основное") == []


def test_variant_records_unchanged():
    records = [
        {"title": "A", "category": "основное", "amount": 4},
        {"title": "B", "category": "дополнительное", "amount": 2},
        {"title": "C", "category": "основное", "amount": 3},
    ]
    original = [record.copy() for record in records]
    totals_by_category(records)
    titles_in_category(records, "основное")
    titles_in_category(records, "нет")
    sorted_totals(records)
    assert records == original


def test_variant_totals():
    assert totals_by_category(RECORDS) == {
        "комнатные": 5,
        "суккуленты": 9,
        "уличные": 18,
    }


def test_variant_titles():
    assert titles_in_category(RECORDS, "суккуленты") == ["Кактус опунция", "Алоэ"]
    assert titles_in_category(RECORDS, "нет") == []


def test_sorted_totals():
    assert sorted_totals(RECORDS) == [
        ("уличные", 18),
        ("суккуленты", 9),
        ("комнатные", 5),
    ]
    records = [
        {"title": "A", "category": "основное", "amount": 4},
        {"title": "B", "category": "дополнительное", "amount": 2},
        {"title": "C", "category": "основное", "amount": 3},
    ]
    assert sorted_totals(records) == [("основное", 7), ("дополнительное", 2)]


def test_sorted_totals_equal_sums():
    records = [
        {"title": "A", "category": "зелёные", "amount": 1},
        {"title": "B", "category": "белые", "amount": 1},
    ]
    assert sorted_totals(records) == [("белые", 1), ("зелёные", 1)]


CHECKS = [
    test_word_counts_basic,
    test_word_counts_punctuation_only,
    test_word_counts_empty,
    test_word_counts_mixed_punctuation,
    test_common_topics,
    test_all_topics,
    test_topics_with_empty_list,
    test_record_and_pair,
    test_totals_example,
    test_titles_example,
    test_totals_empty,
    test_variant_records_unchanged,
    test_variant_totals,
    test_variant_titles,
    test_sorted_totals,
    test_sorted_totals_equal_sums,
]


def main():
    for check in CHECKS:
        check()
        print(f"{check.__name__}: ок")
    print(f"Всего проверок: {len(CHECKS)}, ошибок нет")


if __name__ == "__main__":
    main()
