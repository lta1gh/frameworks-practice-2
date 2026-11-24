"""Тесты работы с документами."""

from pathlib import Path

import pytest

from documents import add_document, search_documents


def test_add_document_saves_data(tmp_path: Path) -> None:
    """Проверяет добавление и сохранение документа."""
    path = tmp_path / "documents.json"

    document = add_document(
        "  Отчёт  ",
        doc_type="Отчёт",
        volume="31",
        data_file=path,
    )

    assert document["name"] == "Отчёт"
    assert document["type"] == "Отчёт"
    assert search_documents("отчет", data_file=path)[0]["name"] == "Отчёт"


def test_add_document_requires_name(tmp_path: Path) -> None:
    """Пустое название документа запрещено."""
    with pytest.raises(ValueError):
        add_document("   ", data_file=tmp_path / "documents.json")


def test_search_documents_partial_and_yo(tmp_path: Path) -> None:
    """Поиск работает по части названия и с заменой 'ё'."""
    path = tmp_path / "documents.json"

    add_document("Отчёт за квартал", data_file=path)
    add_document("Демо-1", data_file=path)

    results = search_documents("ОТЧЕТ", data_file=path)

    assert len(results) == 1
    assert results[0]["name"] == "Отчёт за квартал"


def test_search_documents_rejects_empty_query(tmp_path: Path) -> None:
    """Пустой поисковый запрос запрещён."""
    with pytest.raises(ValueError):
        search_documents("  ", data_file=tmp_path / "documents.json")