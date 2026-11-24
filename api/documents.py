"""Бизнес-логика работы с документами."""

from pathlib import Path
from typing import Any, Dict, List, Optional

from storage import load_data, save_data
from utils import clean_optional, normalize, validate_name

Document = Dict[str, Any]


def add_document(
    name: str,
    doc_type: Optional[str] = None,
    volume: Optional[str] = None,
    author: Optional[str] = None,
    location: Optional[str] = None,
    data_file: Optional[Path] = None,
) -> Document:
    """Добавляет документ и сохраняет его в JSON-файл."""
    cleaned_name = validate_name(name)

    data = load_data(data_file)
    new_doc: Document = {
        "name": cleaned_name,
        "type": clean_optional(doc_type),
        "volume": clean_optional(volume),
        "author": clean_optional(author),
        "location": clean_optional(location),
    }

    data.append(new_doc)
    save_data(data, data_file)
    return new_doc


def search_documents(
    query: str,
    data_file: Optional[Path] = None,
) -> List[Document]:
    """Ищет документы по части названия."""
    if not isinstance(query, str):
        raise ValueError("Поисковый запрос должен быть строкой.")

    cleaned_query = query.strip()
    if not cleaned_query:
        raise ValueError("Поисковый запрос не может быть пустым.")

    query_norm = normalize(cleaned_query)
    data = load_data(data_file)
    results: List[Document] = []

    for document in data:
        if not isinstance(document, dict):
            continue
        name = document.get("name")
        if isinstance(name, str) and query_norm in normalize(name):
            results.append(document)

    return results