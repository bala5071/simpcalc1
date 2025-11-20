"""
Configuration defaults and environment overrides for simpcalc1.
"""
import os
from typing import Dict, Any

HISTORY_FILE_DEFAULT: str = r"C:\Users\balas\Documents\Projects\simpcalc1\data\history.json"
LOG_LEVEL_DEFAULT: str = os.environ.get("LOG_LEVEL", "INFO")
MAX_EXPRESSION_LENGTH: int = int(os.environ.get("MAX_EXPRESSION_LENGTH", "1000"))


def load_from_env() -> Dict[str, Any]:
    """Return configuration values loaded from environment variables if provided.

    Returns a dictionary with keys: history_file, log_level, max_expression_length.
    """
    return {
        "history_file": os.environ.get("SIMPCALC_HISTORY_FILE", HISTORY_FILE_DEFAULT),
        "log_level": os.environ.get("LOG_LEVEL", LOG_LEVEL_DEFAULT),
        "max_expression_length": int(os.environ.get("MAX_EXPRESSION_LENGTH", str(MAX_EXPRESSION_LENGTH))),
    }
