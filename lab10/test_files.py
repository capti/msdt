"""Проверки лабораторной работы 10: python test_files.py"""

from pathlib import Path
from tempfile import TemporaryDirectory

from files_lab import read_matrix, selected_sum
from main import process, read_positive_integer
from table import column_sums, row_sums


def check_invalid(content, expected_text=None):
    """Проверяет, что некорректное содержимое вызывает ValueError."""
    with TemporaryDirectory() as directory:
        path = Path(directory) / "matrix.txt"
        path.write_text(content, encoding="utf-8")
        try:
            read_matrix(path)
        except ValueError as error:
            if expected_text is not None:
                assert expected_text in str(error), (expected_text, str(error))
        else:
            assert False, "Ошибка не обнаружена"


# Обычное чтение (пример из условия)
with TemporaryDirectory() as directory:
    path = Path(directory) / "matrix.txt"
    path.write_text("1 2\n7 -1\n", encoding="utf-8")
    assert read_matrix(path) == [[7, -1]]
print("Проверка чтения пройдена")

# Граничный случай: матрица 1x1
with TemporaryDirectory() as directory:
    path = Path(directory) / "matrix.txt"
    path.write_text("1 1\n0\n", encoding="utf-8")
    assert read_matrix(path) == [[0]]
print("Проверка матрицы 1x1 пройдена")

# Особые случаи: неверный формат
check_invalid("")
check_invalid("0 3\n")
check_invalid("1 2\n1\n", "2")
check_invalid("1 2\n1 x\n", "2")
check_invalid("1 1\n0\n0\n")
check_invalid("1 2\n\n7 -1\n")
print("Проверки неверного формата пройдены")

# Отсутствующий путь: FileNotFoundError в функции, сообщение в основной программе
with TemporaryDirectory() as directory:
    path = Path(directory) / "missing.txt"
    try:
        read_matrix(path)
    except FileNotFoundError:
        pass
    else:
        assert False, "Ошибка не обнаружена"
    assert process(Path(directory)) is False
print("Проверка отсутствующего файла пройдена")

# Индивидуальный вариант 11: сумма последнего столбца
control = [[1, -2, 3], [4, 0, -6]]
assert selected_sum(control) == -3
assert selected_sum([[7]]) == 7
assert selected_sum([]) == 0
assert selected_sum([[1, 2], [3, 4]]) == 6
print("Проверка варианта 11 пройдена")

# Суммы из работы №9
assert row_sums(control) == [2, -2]
assert column_sums(control) == [5, -2, -3]
print("Проверка сумм пройдена")

# Надёжный ввод: abc, 0, -2, 3
values = iter(["abc", "0", "-2", "3"])
messages = []
assert read_positive_integer(lambda prompt: next(values), messages.append) == 3
assert messages == [
    "Нужно ввести целое число",
    "Число должно быть больше нуля",
    "Число должно быть больше нуля",
]
print("Проверка ввода пройдена")

# Сохранность старого отчёта при некорректном входе
with TemporaryDirectory() as directory:
    folder = Path(directory)
    (folder / "matrix.txt").write_text("2 3\n1 -2 3\n4 0 -6\n", encoding="utf-8")
    assert process(folder) is True
    report_path = folder / "report.txt"
    original = report_path.read_text(encoding="utf-8")
    assert "Результат варианта: -3" in original

    csv_text = (folder / "matrix.csv").read_text(encoding="utf-8")
    assert "1,-2,3" in csv_text and "4,0,-6" in csv_text

    (folder / "matrix.txt").write_text("1 2\n1 x\n", encoding="utf-8")
    assert process(folder) is False
    assert report_path.read_text(encoding="utf-8") == original
print("Проверка сохранности отчёта пройдена")

print("Все проверки пройдены")
