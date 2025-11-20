"""
History persistence utilities for simpcalc1.

Provides append_record and read_history functions which operate on JSON files.
Writes are atomic via temporary file + os.replace.
"""
import json
import os
import tempfile
from typing import List

from ..models.record import CalculationRecord


def append_record(record: CalculationRecord, file_path: str) -> None:
    """Append a CalculationRecord to the history JSON file.

    Creates parent directories if necessary. If the file exists and contains
    invalid JSON, it will be overwritten with a list containing the given record.

    Args:
        record: CalculationRecord to append
        file_path: Path to JSON file

    Raises:
        IOError: On filesystem issues.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    data = []
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                if not isinstance(data, list):
                    raise ValueError("History file content must be a JSON list.")
            except json.JSONDecodeError:
                # Malformed JSON: start fresh
                data = []
    data.append(record.__dict__)
    dir_name = os.path.dirname(file_path) or "."
    fd, temp_path = tempfile.mkstemp(dir=dir_name, prefix="history_", suffix=".tmp")
    os.close(fd)
    with open(temp_path, "w", encoding="utf-8") as tf:
        json.dump(data, tf, indent=2, ensure_ascii=False)
    os.replace(temp_path, file_path)


def read_history(file_path: str) -> List[CalculationRecord]:
    """Read history JSON file and return list of CalculationRecord instances.

    Returns empty list if file doesn't exist.

    Raises:
        ValueError: If JSON structure is invalid.
    """
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("History file content must be a JSON list.")
    records: List[CalculationRecord] = []
    for item in data:
        # minimal validation: required keys exist
        records.append(CalculationRecord(**item))
    return records
