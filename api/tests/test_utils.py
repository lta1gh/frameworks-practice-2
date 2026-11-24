"""Тесты вспомогательных функций."""

import pytest

from utils import clean_optional, normalize, validate_name


def test_normalize_lower_and_yo() -> None:
    """Проверяет приведение регистра и замену 'ё'."""
    assert normalize("Ёлка") == "елка"


def test_clean_optional() -> None:
    """Проверяет очистку необязательных полей."""
    assert clean_optional("  текст ") == "текст"
    assert clean_optional("   ") is None
    assert clean_optional(None) is None


def test_validate_name_rejects_empty() -> None:
    """Проверяет запрет пустого названия."""
    with pytest.raises(ValueError):
        validate_name("   ")