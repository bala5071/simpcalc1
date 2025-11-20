"""
Validation utilities for simpcalc1.
"""
from typing import Any
from .exceptions import ValidationError


def validate_expression(expression: Any, max_length: int = 1000) -> None:
    """Validate expression shape and length.

    Raises:
        ValidationError: If expression is empty, not a string, or exceeds max_length.
    """
    if not isinstance(expression, str):
        raise ValidationError("Expression must be a string.")
    if expression.strip() == "":
        raise ValidationError("Expression cannot be empty or whitespace.")
    if len(expression) > max_length:
        raise ValidationError(f"Expression exceeds maximum length of {max_length} characters.")
