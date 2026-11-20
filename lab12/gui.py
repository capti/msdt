"""Дополнительное задание: окно поиска записей. Lab 12 (вариант 11)."""

from pathlib import Path
import tkinter as tk
from tkinter import ttk

from logic import find_records
from storage import load_records


def by_id(record):
    """Ключ сортировки записей по идентификатору."""
    return record["id"]


def search_text(records, query):
    """Готовит текст результата поиска, не завися от tkinter."""
    if not query.strip():
        return "Название не должно быть пустым"
    found = find_records(records, query)
    if not found:
        return "Ничего не найдено"
    lines = []
    for record in sorted(found, key=by_id):
        status = "выполнено" if record["completed"] else "не выполнено"
        lines.append(
            f"{record['id']} | {record['title']} | {record['category']} | "
            f"{record['amount']} раст. | {status}"
        )
    return "\n".join(lines)


def main():
    path = Path(__file__).resolve().parent / "data.json"
    records = load_records(path) if path.exists() else []

    root = tk.Tk()
    root.title("План посадки растений — поиск")
    value = tk.StringVar()
    result = tk.StringVar(value="Введите часть названия")

    def show_result():
        result.set(search_text(records, value.get()))

    ttk.Label(root, text="Часть названия:").pack(padx=12, pady=(12, 4))
    ttk.Entry(root, textvariable=value).pack(padx=12, pady=4)
    ttk.Button(root, text="Найти", command=show_result).pack(pady=8)
    ttk.Label(root, textvariable=result, justify=tk.LEFT).pack(padx=12, pady=(4, 12))
    root.mainloop()


if __name__ == "__main__":
    main()
