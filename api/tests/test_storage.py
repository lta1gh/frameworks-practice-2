"""Тесты JSON-хранилища."""

from pathlib import Path

import pytest

from storage import load_data, save_data


def test_load_missing_file(tmp_path: Path) -> None:
    """Отсутствующий файл читается как пустой список."""
    assert load_data(tmp_path / "missing.json") == []


def test_save_and_load(tmp_path: Path) -> None:
    """Сохранённые данные загружаются обратно."""
    path = tmp_path / "documents.json"
    data = [{"name": "Документ"}]

    save_data(data, path)

    assert load_data(path) == data


def test_load_invalid_json(tmp_path: Path) -> None:
    """Некорректный JSON приводит к RuntimeError."""
    path = tmp_path / "documents.json"
    path.write_text("{bad", encoding="utf-8")

    with pytest.raises(RuntimeError):
        load_data(path)