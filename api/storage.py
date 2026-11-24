"""Работа с JSON-хранилищем документов."""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

Document = Dict[str, Any]
DATA_FILE = Path(__file__).with_name("documents.json")


def _resolve_path(data_file: Optional[Path]) -> Path:
    """Возвращает путь к файлу данных."""
    return data_file if data_file is not None else DATA_FILE


def load_data(data_file: Optional[Path] = None) -> List[Document]:
    """Загружает список документов из JSON-файла."""
    path = _resolve_path(data_file)
    if not path.exists():
        return []

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(
            f"Не удалось загрузить данные из {path}: {exc}"
        ) from exc

    if not isinstance(data, list):
        raise ValueError("JSON-файл должен содержать список документов.")
    return data


def save_data(
    data: List[Document],
    data_file: Optional[Path] = None,
) -> None:
    """Сохраняет список документов в JSON-файл."""
    path = _resolve_path(data_file)

    try:
        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except OSError as exc:
        raise RuntimeError(
            f"Не удалось сохранить данные в {path}: {exc}"
        ) from exc