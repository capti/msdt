"""Ввод-вывод и обработка ошибок для лабораторной работы 10."""

from pathlib import Path

from files_lab import export_csv, read_matrix, selected_sum
from table import column_sums, row_sums


def read_positive_integer(input_function=input, output_function=print):
    """Повторяет ввод, пока не получено целое число больше нуля.

    Различает сообщения «не целое число» и «должно быть больше нуля».
    Необязательные параметры позволяют подставить другой ввод-вывод в проверках;
    при обычном вызове read_positive_integer() используются input и print.
    """
    while True:
        text = input_function("Введите целое число больше нуля: ")
        try:
            number = int(text)
        except ValueError:
            output_function("Нужно ввести целое число")
            continue
        if number <= 0:
            output_function("Число должно быть больше нуля")
            continue
        return number


def build_report(matrix):
    """Формирует текст отчёта в памяти, не открывая файлы на запись."""
    row_line = " ".join(str(value) for value in row_sums(matrix))
    column_line = " ".join(str(value) for value in column_sums(matrix))
    return (
        f"Суммы строк: {row_line}\n"
        f"Суммы столбцов: {column_line}\n"
        f"Результат варианта: {selected_sum(matrix)}\n"
    )


def process(folder):
    """Читает вход, проверяет данные и только затем записывает отчёт и CSV.

    Возвращает True при успешной записи и False при любой ожидаемой ошибке.
    Входной файл открывается только для чтения.
    """
    source = folder / "matrix.txt"
    report = folder / "report.txt"
    csv_path = folder / "matrix.csv"

    try:
        matrix = read_matrix(source)
    except FileNotFoundError:
        print(f"Ошибка: файл {source} не найден. Отчёт не изменён.")
        return False
    except UnicodeError:
        print(f"Ошибка: неверная кодировка файла {source}. Отчёт не изменён.")
        return False
    except ValueError as error:
        print(f"Ошибка формата файла {source}: {error}. Отчёт не изменён.")
        return False
    except OSError as error:
        print(f"Ошибка доступа к файлу {source}: {error}. Отчёт не изменён.")
        return False

    report_text = build_report(matrix)
    try:
        report.write_text(report_text, encoding="utf-8")
        export_csv(matrix, csv_path)
    except OSError as error:
        print(f"Ошибка записи: {error}")
        return False

    print(f"Отчёт записан в {report}:")
    print(report_text, end="")
    print(f"CSV записан в {csv_path}")
    return True


def main():
    folder = Path(__file__).resolve().parent
    process(folder)


if __name__ == "__main__":
    main()
