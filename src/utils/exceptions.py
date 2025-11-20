"""
Custom exceptions for simpcalc1.
"""

class CalculatorError(Exception):
    """Base class for calculator errors."""


class ParseError(CalculatorError):
    """Raised when parsing of the expression fails."""

    def __init__(self, message: str) -> None:
        super().__init__(message)


class EvaluationError(CalculatorError):
    """Raised when evaluation fails (e.g., divide by zero)."""

    def __init__(self, message: str) -> None:
        super().__init__(message)


class ValidationError(CalculatorError):
    """Raised on invalid input parameters."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
