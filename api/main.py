"""CLI-приложение DocLib."""

from typing import Any, Dict

from documents import add_document, search_documents
from storage import load_data


def print_document(index: int, document: Dict[str, Any]) -> None:
    """Печатает один документ."""
    print(f"{index}. Название: {document.get('name', '')}")

    fields = (
        ("type", "Тип"),
        ("volume", "Объем"),
        ("author", "Автор"),
        ("location", "Место хранения"),
    )

    for key, title in fields:
        value = document.get(key)
        if value:
            print(f"   {title}: {value}")

    print()


def run() -> None:
    """Запускает интерактивный режим."""
    try:
        documents = load_data()
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"Ошибка загрузки данных: {exc}")
        return

    print("Добро пожаловать в систему управления документами.")
    print(f"Загружено документов: {len(documents)}")

    while True:
        print("\nВыберите действие:")
        print("1. Добавить документ")
        print("2. Поиск документов по названию")
        print("3. Выйти")

        try:
            choice = input("Введите номер действия: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nВыключение...")
            break

        if choice == "1":
            try:
                name = input(
                    "Введите название документа (обязательно): "
                ).strip()
                doc_type = input(
                    "Введите тип документа (Enter для пропуска): "
                ).strip()
                volume = input(
                    "Введите объем документа (Enter для пропуска): "
                ).strip()
                author = input(
                    "Введите автора документа (Enter для пропуска): "
                ).strip()
                location = input(
                    "Введите место хранения (Enter для пропуска): "
                ).strip()

                add_document(
                    name,
                    doc_type or None,
                    volume or None,
                    author or None,
                    location or None,
                )
            except (EOFError, KeyboardInterrupt):
                print("\nВыключение...")
                break
            except (ValueError, RuntimeError) as exc:
                print(f"Ошибка: {exc}")
            else:
                print(f"Документ '{name.strip()}' успешно добавлен.")

        elif choice == "2":
            try:
                query = input(
                    "Введите название или часть названия: "
                ).strip()
                results = search_documents(query)
            except (EOFError, KeyboardInterrupt):
                print("\nВыключение...")
                break
            except (ValueError, RuntimeError) as exc:
                print(f"Ошибка: {exc}")
            else:
                if results:
                    print(f"\nНайдено документов: {len(results)}")
                    for index, document in enumerate(results, 1):
                        print_document(index, document)
                else:
                    print("Документы не найдены.")

        elif choice == "3":
            print("Выключение...")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    run()