"""Вспомогательные функции."""

from typing import Optional


def normalize(text: str) -> str:
    """Приводит строку к нижнему регистру и заменяет 'ё' на 'е'."""
    return text.lower().replace("ё", "е")


def clean_optional(value: Optional[str]) -> Optional[str]:
    """Очищает необязательное строковое поле."""
    if value is None:
        return None
    cleaned = value.strip()
    return cleaned or None


def validate_name(name: str) -> str:
    """Проверяет и возвращает очищенное название документа."""
    if not isinstance(name, str):
        raise ValueError("Название документа должно быть строкой.")
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("Название документа обязательно.")
    return cleaned