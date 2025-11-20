"""
Data model for calculation records persisted to history JSON.
"""
from dataclasses import dataclass
from typing import Optional, Union
import datetime
import uuid


@dataclass
class CalculationRecord:
    id: str
    expression: str
    result: Union[int, float, str]
    success: bool
    error_type: Optional[str]
    error_message: Optional[str]
    timestamp: str

    @staticmethod
    def create(
        expression: str,
        result: Union[int, float, str],
        success: bool,
        error_type: Optional[str] = None,
        error_message: Optional[str] = None,
        timestamp: Optional[str] = None,
        id: Optional[str] = None,
    ) -> "CalculationRecord":
        """Factory helper to create a CalculationRecord with defaults.

        - id: generated UUID4 string if not provided
        - timestamp: current UTC ISO8601 'Z' suffix if not provided
        """
        if not isinstance(expression, str) or expression.strip() == "":
            raise ValueError("Expression must be a non-empty string")
        if success and (error_type is not None or error_message is not None):
            raise ValueError("Successful record cannot have error information")
        return CalculationRecord(
            id=id or str(uuid.uuid4()),
            expression=expression,
            result=result,
            success=success,
            error_type=error_type,
            error_message=error_message,
            timestamp=timestamp or datetime.datetime.utcnow().isoformat() + "Z",
        )
