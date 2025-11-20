"""
Public API for simpcalc1: Calculator class for programmatic use.
"""
from typing import Optional

from .models.record import CalculationRecord
from .core.calculator import evaluate_expression
from .storage.history import append_record
from .config import settings
from .utils.exceptions import ParseError, EvaluationError, ValidationError
from .utils.validators import validate_expression


class Calculator:
    """Public calculator API.

    Example:
        calc = Calculator()
        record = calc.evaluate("1+2*3", persist=True)
    """

    def __init__(self, history_file: Optional[str] = None) -> None:
        """Initialize Calculator with optional history file path.

        If history_file is None, the default from settings is used.
        """
        self.history_file = history_file or settings.HISTORY_FILE_DEFAULT

    def evaluate(self, expression: str, persist: bool = False) -> CalculationRecord:
        """Evaluate an expression and return a CalculationRecord.

        Args:
            expression: Expression string to evaluate.
            persist: If True, append result (or error) to history JSON file.

        Returns:
            CalculationRecord representing the evaluation result.

        Raises:
            ValidationError: If input fails validation.
            ParseError: If tokenization/parsing fails.
            EvaluationError: If evaluation fails (e.g., divide by zero).
        """
        validate_expression(expression, max_length=settings.MAX_EXPRESSION_LENGTH)
        try:
            result = evaluate_expression(expression)
            record = CalculationRecord.create(expression=expression, result=result, success=True)
            if persist:
                append_record(record, self.history_file)
            return record
        except (ParseError, EvaluationError, ValidationError):
            # Create non-successful record and persist if requested, then re-raise
            import traceback

            exc_type = None
            exc_msg = None
            try:
                raise
            except BaseException as ex:  # pragma: no cover - capture current exception
                exc_type = ex.__class__.__name__
                exc_msg = str(ex)
            record = CalculationRecord.create(
                expression=expression,
                result=exc_msg or "",
                success=False,
                error_type=exc_type,
                error_message=exc_msg,
            )
            if persist:
                append_record(record, self.history_file)
            # Re-raise the original exception so callers can handle it
            raise
