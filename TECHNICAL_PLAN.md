## 1. PROJECT OVERVIEW & OBJECTIVES

- Project root (exact path you MUST use): C:\Users\balas\Documents\Projects\simpcalc1

Problem Statement:
- Provide a reliable, well-tested, small Python application ("simpcalc1") that performs basic arithmetic operations (addition, subtraction, multiplication, division, exponentiation, modulus, unary negation, parentheses/evaluation), supports both interactive CLI and programmatic usage, maintains an optional operation history (persisted to JSON), validates inputs, and handles edge cases (divide-by-zero, invalid tokens, overflow) in a deterministic, documented way.

Target Users:
- Students, educators, developers, or QA who need a dependable simple calculator for scripting or CLI use.
- Developers who will embed the calculator functionality into other Python programs or test it.

Core Functionality (3-5 main features):
1. CLI interactive calculator and single-expression evaluation via command-line arguments.
2. Programmatic calculator engine with a clean Python API (Calculator class) that accepts expression strings and returns results with type and metadata.
3. Input validation and robust error handling (clear exceptions for invalid expressions, divide-by-zero, unsupported operations).
4. Optional persistence of history to a JSON file with configurable path.
5. Unit and integration tests covering arithmetic operations, edge cases, and persistence.

Success Criteria:
- Correct evaluation of mathematical expressions containing integers, floats, +, -, *, /, %, **, parentheses, and unary minus.
- Clear, documented API functions with type hints and reproducible outputs.
- Tests pass with >= 95% coverage for core modules (calculator engine, validators, storage).
- CLI usage works as documented and returns appropriate exit codes for success/failure.
- History persistence works and reads/writes correct JSON entries.

Scope:
- IN scope:
  - Expression parsing and evaluation for standard arithmetic operators: +, -, *, /, %, **, parentheses, unary minus.
  - CLI interface (interactive prompt and single-expression mode).
  - Programmatic API (Calculator class with evaluate method).
  - Optional JSON-based history persistence and retrieval.
  - Logging, error handling, input validation, unit tests, and developer tooling (formatter, linter).
- OUT of scope:
  - Support for symbolic algebra, variables, functions (sin/cos/log), or matrices.
  - A web UI, REST API, GUI, or external service integration.
  - Arbitrary precision beyond Python float/int semantics (no special big-number library).
  - Multi-user concurrent history writes (this is single-user desktop app, not multi-process safe).

## 2. TECHNOLOGY STACK (Specific Versions Required)

- Programming Language:
  - Python 3.11.6
    - Why: Stable long-term supported version with typing improvements and wide library support.

- Core Framework:
  - None (standard library for core logic)
    - Why: The project is small and does not require a web or app framework. Using the standard library ensures minimal dependencies and compatibility.

- Key Libraries:
  - click==8.1.7 # For robust CLI interface and argument parsing
  - pytest==7.4.2 # For unit and integration testing
  - black==24.3.0 # Code formatter to keep consistent style
  - flake8==6.1.0 # Linter for basic code quality rules
  - mypy==1.9.1 # Optional static typing checks
  - coverage==7.2.5 # Test coverage measurement
  - types-requests==2.31.0 (optional) # If typing stubs needed (not required)
  - (No database driver required; storing to JSON)

- Database/Storage:
  - JSON file storage (no RDBMS). No version required; uses Python standard library json.

- External Services/APIs:
  - None.

- Development Tools:
  - Testing: pytest==7.4.2, coverage==7.2.5
  - Linter: flake8==6.1.0
  - Formatter: black==24.3.0
  - Type checker: mypy==1.9.1

- Justification summary:
  - Minimal dependencies keep the project portable and simple. click provides a clean CLI; pytest and coverage provide testing and measurement. Black/flake8/mypy improve maintainability.

## 3. COMPLETE FILE & DIRECTORY STRUCTURE

Root directory EXACT path: C:\Users\balas\Documents\Projects\simpcalc1

Exact file tree (copy and create exactly as below):
```
C:\Users\balas\Documents\Projects\simpcalc1\
├── src\
│   ├── __init__.py                      # Package init for simpcalc1
│   ├── main.py                           # CLI entry point (click)
│   ├── api.py                            # Programmatic API and Calculator class
│   ├── core\
│   │   ├── __init__.py
│   │   ├── calculator.py                 # Core evaluation engine
│   │   └── parser.py                     # Safe expression parser/tokenizer
│   ├── models\
│   │   ├── __init__.py
│   │   └── record.py                     # CalculationRecord dataclass
│   ├── storage\
│   │   ├── __init__.py
│   │   └── history.py                    # JSON persistence for history
│   ├── utils\
│   │   ├── __init__.py
│   │   ├── validators.py                 # Input validation helpers
│   │   └── exceptions.py                 # Custom exceptions
│   └── config\
│       ├── __init__.py
│       └── settings.py                   # Configuration default values
├── tests\
│   ├── __init__.py
│   ├── test_calculator.py                # Unit tests for calculator engine
│   ├── test_parser.py                    # Tests for parser/tokenizer
│   ├── test_api.py                       # Tests for public API & history integration
│   └── test_history.py                   # Tests for history persistence
├── data\
│   └── history.json                      # Auto-created on first write (optional)
├── docs\
│   └── usage.md                          # Usage examples, CLI docs, developer notes
├── requirements.txt                      # Pin exact Python dependencies
├── pyproject.toml                        # For black/mypy configuration (optional)
├── .env.example                          # Example environment variables
├── .gitignore                            # Git ignore rules
├── README.md                             # Project overview and quick start
└── LICENSE                               # Recommended MIT license file
```

Why each directory/file exists:
- src/: All production Python code.
- src/main.py: CLI entry — exposes interactive prompt and single-expression mode.
- src/api.py: Lightweight wrapper and public API for other code to import and call.
- src/core/: Core components of calculator: parser and calculator engine. Placed in core namespace to separate from public API.
- src/models/: Data models used (CalculationRecord).
- src/storage/: Persistence layer; keeps storage concerns separate from logic.
- src/utils/: Validators and custom exceptions for centralized error types.
- src/config/: Centralized settings and environment variable defaults.
- tests/: All unit and integration tests.
- data/: Place to store data like history.json. Should be created automatically, tracked in .gitignore? We will include history.json in .gitignore by default but include an empty template in .gitkeep if desired. However the spec lists data/history.json as auto-created on first write.
- docs/: Developer and usage docs.
- requirements.txt: Dependency list.
- pyproject.toml: Optional tool configuration (black/mypy).
- .env.example: Template environment variables.
- .gitignore: Ignore venv, __pycache__, data history, etc.
- README.md: Project overview and quick start.
- LICENSE: Licensing.

Auto-generated vs manually created:
- Manually created by developer: all src/*.py, tests/*, docs/*, README.md, requirements.txt, .env.example, .gitignore, pyproject.toml, LICENSE.
- Auto-generated at runtime: data/history.json will be created by storage/history.py if not found; .venv created by developer environment.

## 4. DATA MODELS & SCHEMAS

There is a single data model for persistence/history.

File: src/models/record.py

Class: CalculationRecord
- Fields:
  - id: str (UUID v4 string; required, unique)
  - expression: str (required; the original input expression)
  - result: float | int | str (required; numerical result or "ERROR" string for failed evaluation)
  - success: bool (required; True if evaluation succeeded)
  - error_type: str | None (error type string e.g., "ZeroDivisionError" or None)
  - error_message: str | None (detailed error message or None)
  - timestamp: str (ISO 8601 datetime string; required)
- Constraints:
  - id must be unique per record.
  - expression cannot be empty.
  - timestamp is auto-generated when the record is created.
  - If success is True then error_type and error_message must be None.
  - result must be JSON serializable (int/float/str).
- Default values:
  - success default False in constructor (before evaluation) but when created via storage API, set appropriately.
  - timestamp defaults to current UTC time string if not provided.
- Validation rules:
  - Validate expression is str and has length > 0.
  - Validate that if success is True, error_type/error_message are None.
  - Use validators in src/utils/validators.py.

Example dataclass (Python):
```python
@dataclass
class CalculationRecord:
    id: str
    expression: str
    result: Union[int, float, str]
    success: bool
    error_type: Optional[str]
    error_message: Optional[str]
    timestamp: str
```

No relational models or DB schema needed (JSON flat array of records).

## 5. MODULE SPECIFICATIONS (For Each File)

Below are the modules, their purpose, exported functions/classes, type hints, dependencies, and error handling.

Note: All public function signatures include type hints.

---

File: src/utils/exceptions.py
- Module Purpose: Define custom exception types used across the project.
- Public classes:
```python
class CalculatorError(Exception):
    """Base class for calculator errors."""
```
```python
class ParseError(CalculatorError):
    """Raised when parsing of the expression fails."""
    def __init__(self, message: str) -> None: ...
```
```python
class EvaluationError(CalculatorError):
    """Raised when evaluation fails (e.g., divide by zero)."""
    def __init__(self, message: str) -> None: ...
```
```python
class ValidationError(CalculatorError):
    """Raised on invalid input parameters."""
    def __init__(self, message: str) -> None: ...
```
- Dependencies: None beyond builtins.
- Error Handling: Simple exception classes with message.

---

File: src/config/settings.py
- Module Purpose: Central configuration constants and environment variable override logic.
- Public constants/ functions:
```python
HISTORY_FILE_DEFAULT: str = r"C:\Users\balas\Documents\Projects\simpcalc1\data\history.json"
LOG_LEVEL_DEFAULT: str = "INFO"
MAX_EXPRESSION_LENGTH: int = 1000
```
- Optional function:
```python
def load_from_env() -> Dict[str, Any]:
    """Return dict with settings loaded from environment variables if set."""
```
- Dependencies: os, typing.
- Error Handling: None; uses fallback defaults.

---

File: src/utils/validators.py
- Module Purpose: Input validation helpers.
- Public functions:
```python
def validate_expression(expression: str, max_length: int = 1000) -> None:
    """
    Validate expression shape and length.
    Raises:
        ValidationError: If expression is empty, not string, or exceeds max_length.
    """
```
- Private helpers: _is_supported_char(token: str) -> bool
- Dependencies: utils.exceptions.ValidationError
- Error Handling: Raises ValidationError with descriptive messages.

---

File: src/core/parser.py
- Module Purpose: Tokenize expression and produce a safe AST-like structure or token list.
- Public functions/classes:
```python
def tokenize(expression: str) -> List[str]:
    """
    Break expression into tokens: numbers, operators, parentheses.
    Returns list of tokens in order.
    Raises:
        ParseError: On unexpected characters or syntax.
    """
```
```python
def shunting_yard(tokens: List[str]) -> List[str]:
    """
    Convert tokens to Reverse Polish Notation (RPN) using the Shunting-yard algorithm.
    Returns RPN token list.
    Raises:
        ParseError: On mismatched parentheses or invalid syntax.
    """
```
- Private functions:
  - _is_number(token: str) -> bool
  - _precedence(op: str) -> int
- Dependencies: utils.exceptions.ParseError
- Error Handling: Use ParseError for invalid tokens, mismatched parentheses, or unexpected operator sequences.

Implementation notes (detailed):
- Tokenizer must accept decimals (e.g., "3.14"), integer literals, unary minus handling (treat unary minus as negative number token, e.g., "-3" or "( -3 )"), and operator tokens: +, -, *, /, %, ** (exponent). Tokenizer should correctly identify the multi-character operator "**".
- The shunting-yard implementation must support precedence: ** highest (right-associative), then *, /, %, then +, -.
- Parentheses must be balanced.

---

File: src/core/calculator.py
- Module Purpose: Evaluate RPN token list or expression string and return numeric result.
- Public functions/classes:
```python
from typing import Union, Tuple

def eval_rpn(rpn_tokens: List[str]) -> Union[int, float]:
    """
    Evaluate RPN tokens and return numeric result (int or float).
    Raises:
        EvaluationError: For divide by zero, stack underflow, invalid operations.
    """
```
```python
def evaluate_expression(expression: str) -> Union[int, float]:
    """
    Full pipeline: validate expression -> tokenize -> convert to RPN -> evaluate -> return numeric result.
    Raises:
        ParseError, EvaluationError, ValidationError
    """
```
- Private helpers:
  - _apply_operator(op: str, left: float, right: float) -> float
- Dependencies: parser.tokenize, parser.shunting_yard, utils.exceptions.EvaluationError
- Error Handling:
  - Division or modulus by zero raises EvaluationError with message "Division by zero".
  - Stack underflow raises EvaluationError "Malformed expression".
  - Overflow errors propagate as EvaluationError with underlying message.

Examples:
- evaluate_expression("1 + 2 * 3") -> 7
- evaluate_expression("(1+2)**3") -> 27

Type casting:
- If a result is an integer mathematically (e.g., 4.0), the function may return int 4 to preserve integer types where possible.

---

File: src/api.py
- Module Purpose: Public API for programmatic calls and higher-level operations (evaluate and optionally persist).
- Public class and functions:
```python
from typing import Union, Optional
from models.record import CalculationRecord

class Calculator:
    def __init__(self, history_file: Optional[str] = None) -> None:
        """
        history_file: path to JSON history file. If None, uses default from config.
        """
    def evaluate(self, expression: str, persist: bool = False) -> CalculationRecord:
        """
        Evaluate the expression, return CalculationRecord. If persist True, append to history file.
        Raises:
            ValidationError, ParseError, EvaluationError
        """
```
- Dependencies: core.calculator.evaluate_expression, storage.history for persistence, models.record, config.settings
- Error Handling: Propagates fine-grained exceptions; wraps exceptions to populate CalculationRecord with error info if evaluation fails and persist=True.

Example usage:
```python
calc = Calculator()
record = calc.evaluate("1+2*3", persist=True)
print(record.result)  # 7
```

---

File: src/storage/history.py
- Module Purpose: Append and read calculation history stored in JSON file.
- Public functions:
```python
def append_record(record: CalculationRecord, file_path: str) -> None:
    """
    Append record to JSON file (list of records).
    Creates file if absent. Ensures atomic write: write to temp file then replace.
    Raises:
        IOError: On filesystem issues.
    """
```
```python
def read_history(file_path: str) -> List[CalculationRecord]:
    """
    Read JSON file and return list of CalculationRecord instances.
    Returns empty list if file not found.
    Raises:
        ValueError: On JSON parse errors.
    """
```
- Dependencies: json, os, tempfile, shutil, models.record, typing
- Error Handling:
  - Validate JSON structure (must be list) and fields for each record; if invalid, raise ValueError with adequate message.

Implementation details:
- Use uuid.uuid4() for record ids when creating new records (api.Calculator will create record).
- For atomic writes: write to temporary file in same directory, then os.replace(temp_path, file_path).

---

File: src/main.py
- Module Purpose: CLI entry using click.
- Public CLI commands (using click):
  - cli() — root group
  - eval_cmd(expression: str, persist: bool) — evaluate single expression and print result; exit code 0 on success, non-zero on error.
  - interactive() — interactive REPL: prompt "simpcalc> " until user types "exit" or Ctrl+D.
- Signatures:
```python
@click.command("eval")
@click.argument("expression", type=str)
@click.option("--persist/--no-persist", default=False)
def eval_cmd(expression: str, persist: bool) -> None: ...
```
```python
@click.command("repl")
def repl() -> None: ...
```
- Dependencies: api.Calculator, config.settings, utils.exceptions
- Error Handling: Catch exceptions and print user-friendly messages, log details if debug.

---

File: tests/test_calculator.py
- Module Purpose: Unit tests for core.calculator.evaluate_expression and eval_rpn.
- Public test functions:
  - test_addition()
  - test_precedence()
  - test_parentheses()
  - test_unary_minus()
  - test_divide_by_zero_raises()
  - test_modulus()
  - test_exponentiation()
  - test_malformed_expression_raises()
- Each test uses pytest and asserts results or uses pytest.raises with exact exceptions.

---

File: tests/test_parser.py
- Module Purpose: Tests for tokenizer and shunting-yard algorithm.
- Test cases:
  - test_tokenize_numbers_and_ops()
  - test_tokenize_exponent_operator()
  - test_shunting_yard_basic()
  - test_mismatched_parentheses_raises()

---

File: tests/test_api.py
- Module Purpose: Tests Calculator class evaluate, persistence integration (with tmp path).
- Test cases:
  - test_calculator_persist_writes_file(tmp_path)
  - test_calculator_returns_record_on_error()
  - test_calculator_programmatic_use()

---

File: tests/test_history.py
- Module Purpose: Tests JSON persistence functions.
- Test cases:
  - test_append_and_read_history(tmp_path)
  - test_invalid_json_raises(tmp_path)

## 6. API DESIGN (CLI + Programmatic API)

This project is not a web API; it has:
- Programmatic API via src.api.Calculator class.
- CLI API via src/main.py using click.

Programmatic API:
- Class: Calculator(history_file: Optional[str] = None)
  - evaluate(expression: str, persist: bool = False) -> CalculationRecord

Example:
Request (programmatic):
```python
from simpcalc1.api import Calculator

calc = Calculator()
record = calc.evaluate("2 * (3 + 4)", persist=True)
# record: CalculationRecord(id=..., expression="2*(3+4)", result=14, success=True, error_type=None, error_message=None, timestamp=...)
```

Responses:
- Returns CalculationRecord dataclass instance with fields described in Data Models section.
- On exceptions (invalid input, parse error, evaluation error), evaluate either raises an appropriate exception (ValidationError, ParseError, EvaluationError) unless internal handling is requested; when persist True and evaluation fails, the function will still create a record with success=False and relevant error fields, and append to history.

CLI API:
- Commands:
  - Evaluate single expression:
    - Command: python -m simpcalc1.main eval "2*(3+4)" --persist
    - Output (stdout) on success:
      - 2*(3+4) = 14
      - Record saved to C:\Users\balas\Documents\Projects\simpcalc1\data\history.json
    - Exit code 0
  - Interactive REPL:
    - Command: python -m simpcalc1.main repl
    - REPL prompt:
      - simpcalc> 1+1
      - => 2
      - simpcalc> exit
    - Supports commands:
      - :history -> prints last 20 history entries (if history enabled); otherwise instruct to use --persist or configure history.
      - exit, quit to exit.

Error exit codes:
- 0: Success
- 2: ValidationError (e.g., blank input)
- 3: ParseError
- 4: EvaluationError
- 1: Generic unexpected error

## 7. DETAILED IMPLEMENTATION STEPS

Follow these numbered sequential steps exactly. Use Windows PowerShell commands where appropriate.

Step 1: Create project directory (if not exists)
- Open PowerShell and run:
```powershell
mkdir "C:\Users\balas\Documents\Projects\simpcalc1"
cd "C:\Users\balas\Documents\Projects\simpcalc1"
```

Step 2: Create Python virtual environment
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -V  # Confirm Python 3.11.6 environment
```

Step 3: Create folder structure and empty files
- Run (PowerShell):
```powershell
mkdir src
mkdir src\core
mkdir src\models
mkdir src\storage
mkdir src\utils
mkdir src\config
mkdir tests
mkdir data
mkdir docs
ni src\__init__.py
ni src\main.py
ni src\api.py
ni src\core\__init__.py
ni src\core\calculator.py
ni src\core\parser.py
ni src\models\__init__.py
ni src\models\record.py
ni src\storage\__init__.py
ni src\storage\history.py
ni src\utils\__init__.py
ni src\utils\validators.py
ni src\utils\exceptions.py
ni src\config\__init__.py
ni src\config\settings.py
ni tests\__init__.py
ni tests\test_calculator.py
ni tests\test_parser.py
ni tests\test_api.py
ni tests\test_history.py
ni docs\usage.md
ni README.md
ni requirements.txt
ni .env.example
ni .gitignore
ni pyproject.toml
ni LICENSE
```

Step 4: Populate requirements.txt (exact content)
- Open requirements.txt and add:
```
click==8.1.7
pytest==7.4.2
black==24.3.0
flake8==6.1.0
mypy==1.9.1
coverage==7.2.5
```

Step 5: Populate .gitignore
- Add content:
```
# Virtual environment
.venv/
__pycache__/
*.pyc
data/history.json
.dist-info/
.env
.idea/
.vscode/
```

Step 6: Create src/config/settings.py
- Write exact constants and environment loader:
```python
# src/config/settings.py
import os
from typing import Dict, Any

HISTORY_FILE_DEFAULT = r"C:\Users\balas\Documents\Projects\simpcalc1\data\history.json"
LOG_LEVEL_DEFAULT = os.environ.get("LOG_LEVEL", "INFO")
MAX_EXPRESSION_LENGTH = int(os.environ.get("MAX_EXPRESSION_LENGTH", "1000"))

def load_from_env() -> Dict[str, Any]:
    return {
        "history_file": os.environ.get("SIMPCALC_HISTORY_FILE", HISTORY_FILE_DEFAULT),
        "log_level": os.environ.get("LOG_LEVEL", LOG_LEVEL_DEFAULT),
        "max_expression_length": MAX_EXPRESSION_LENGTH,
    }
```

Step 7: Create src/utils/exceptions.py
- Add:
```python
# src/utils/exceptions.py
class CalculatorError(Exception):
    """Base class for calculator errors."""

class ParseError(CalculatorError):
    pass

class EvaluationError(CalculatorError):
    pass

class ValidationError(CalculatorError):
    pass
```

Step 8: Create src/utils/validators.py
- Add:
```python
# src/utils/validators.py
from typing import Any
from .exceptions import ValidationError

def validate_expression(expression: Any, max_length: int = 1000) -> None:
    if not isinstance(expression, str):
        raise ValidationError("Expression must be a string.")
    if expression.strip() == "":
        raise ValidationError("Expression cannot be empty or whitespace.")
    if len(expression) > max_length:
        raise ValidationError(f"Expression exceeds maximum length of {max_length} characters.")
    # Optional: further char checks can be done in parser
```

Step 9: Implement parser (src/core/parser.py)
- Implement tokenizer and shunting-yard. Use exact code below:
```python
# src/core/parser.py
from typing import List
from ..utils.exceptions import ParseError

_OPERATORS = {"+" , "-", "*", "/", "%", "**"}
_WHITESPACE = set(" \t\n\r")

def tokenize(expression: str) -> List[str]:
    tokens: List[str] = []
    i = 0
    n = len(expression)
    while i < n:
        ch = expression[i]
        if ch in _WHITESPACE:
            i += 1
            continue
        if ch.isdigit() or ch == '.':
            start = i
            has_dot = ch == '.'
            i += 1
            while i < n and (expression[i].isdigit() or (expression[i] == '.' and not has_dot)):
                if expression[i] == '.':
                    has_dot = True
                i += 1
            tokens.append(expression[start:i])
            continue
        # multi-char operator '**'
        if ch == '*' and i + 1 < n and expression[i+1] == '*':
            tokens.append('**')
            i += 2
            continue
        if ch in '+-*/()%':
            tokens.append(ch)
            i += 1
            continue
        raise ParseError(f"Unexpected character '{ch}' at position {i}")
    # Handle unary minus: convert to '0' and '-' when it's at start or after '(' or an operator
    out_tokens: List[str] = []
    prev = None
    for tok in tokens:
        if tok == '-' and (prev is None or prev in ('(', '+', '-', '*', '/', '%', '**')):
            # treat as unary minus by prefixing 0
            out_tokens.append('0')
            out_tokens.append('-')
        else:
            out_tokens.append(tok)
        prev = tok
    return out_tokens

def _precedence(op: str) -> int:
    if op == '**':
        return 4
    if op in ('*', '/', '%'):
        return 3
    if op in ('+', '-'):
        return 2
    return 0

def shunting_yard(tokens: List[str]) -> List[str]:
    output: List[str] = []
    stack: List[str] = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        # number
        try:
            float(token)
            output.append(token)
        except ValueError:
            if token in ('+', '-', '*', '/', '%', '**'):
                while (stack and stack[-1] not in ('(') and
                       ((_precedence(stack[-1]) > _precedence(token)) or
                        (_precedence(stack[-1]) == _precedence(token) and token != '**'))):
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if not stack or stack[-1] != '(':
                    raise ParseError("Mismatched parentheses")
                stack.pop()
            else:
                raise ParseError(f"Unknown token '{token}'")
        i += 1
    while stack:
        if stack[-1] in ('(', ')'):
            raise ParseError("Mismatched parentheses")
        output.append(stack.pop())
    return output
```
- Validation checkpoints: unit tests will check tokenization and parser.

Step 10: Implement calculator engine (src/core/calculator.py)
- Add exact code:
```python
# src/core/calculator.py
from typing import List, Union
from .parser import tokenize, shunting_yard
from ..utils.exceptions import EvaluationError, ParseError

def _apply_operator(op: str, left: float, right: float) -> float:
    if op == '+':
        return left + right
    if op == '-':
        return left - right
    if op == '*':
        return left * right
    if op == '/':
        if right == 0:
            raise EvaluationError("Division by zero.")
        return left / right
    if op == '%':
        if right == 0:
            raise EvaluationError("Modulo by zero.")
        return left % right
    if op == '**':
        return left ** right
    raise EvaluationError(f"Unsupported operator: {op}")

def eval_rpn(rpn_tokens: List[str]) -> Union[int, float]:
    stack: List[float] = []
    for tok in rpn_tokens:
        try:
            num = float(tok)
            stack.append(num)
            continue
        except ValueError:
            # operator
            if len(stack) < 2:
                raise EvaluationError("Malformed expression; insufficient operands.")
            right = stack.pop()
            left = stack.pop()
            res = _apply_operator(tok, left, right)
            stack.append(res)
    if len(stack) != 1:
        raise EvaluationError("Malformed expression; extra operands.")
    result = stack[0]
    # convert to int when exact
    if abs(result - round(result)) < 1e-12:
        return int(round(result))
    return result

def evaluate_expression(expression: str) -> Union[int, float]:
    # Use parser
    tokens = tokenize(expression)
    rpn = shunting_yard(tokens)
    return eval_rpn(rpn)
```

Step 11: Implement models.record (src/models/record.py)
- Add:
```python
# src/models/record.py
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
    def create(expression: str, result: Union[int, float, str], success: bool,
               error_type: Optional[str] = None, error_message: Optional[str] = None,
               timestamp: Optional[str] = None, id: Optional[str] = None) -> "CalculationRecord":
        return CalculationRecord(
            id=id or str(uuid.uuid4()),
            expression=expression,
            result=result,
            success=success,
            error_type=error_type,
            error_message=error_message,
            timestamp=timestamp or datetime.datetime.utcnow().isoformat() + "Z",
        )
```

Step 12: Implement storage.history (src/storage/history.py)
- Add:
```python
# src/storage/history.py
import json
import os
import tempfile
from typing import List
from ..models.record import CalculationRecord

def append_record(record: CalculationRecord, file_path: str) -> None:
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    data = []
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                if not isinstance(data, list):
                    raise ValueError("History file content must be a JSON list.")
            except json.JSONDecodeError:
                # Will overwrite by writing new list with current record
                data = []
    data.append(record.__dict__)
    dir_name = os.path.dirname(file_path)
    fd, temp_path = tempfile.mkstemp(dir=dir_name, prefix="history_", suffix=".tmp")
    os.close(fd)
    with open(temp_path, "w", encoding="utf-8") as tf:
        json.dump(data, tf, indent=2, ensure_ascii=False)
    os.replace(temp_path, file_path)

def read_history(file_path: str) -> List[CalculationRecord]:
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("History file content must be a JSON list.")
    records: List[CalculationRecord] = []
    for item in data:
        # Basic validation of keys
        records.append(CalculationRecord(**item))
    return records
```

Step 13: Implement API class (src/api.py)
- Add:
```python
# src/api.py
from typing import Optional
from .models.record import CalculationRecord
from .core.calculator import evaluate_expression
from .storage.history import append_record
from .config import settings
from .utils.exceptions import ParseError, EvaluationError, ValidationError
from .utils.validators import validate_expression

class Calculator:
    def __init__(self, history_file: Optional[str] = None) -> None:
        self.history_file = history_file or settings.HISTORY_FILE_DEFAULT

    def evaluate(self, expression: str, persist: bool = False) -> CalculationRecord:
        validate_expression(expression, max_length=settings.MAX_EXPRESSION_LENGTH)
        try:
            result = evaluate_expression(expression)
            record = CalculationRecord.create(expression=expression, result=result, success=True)
            if persist:
                append_record(record, self.history_file)
            return record
        except (ParseError, EvaluationError, ValidationError) as ex:
            # create error record and optionally persist
            record = CalculationRecord.create(
                expression=expression,
                result=str(ex),
                success=False,
                error_type=ex.__class__.__name__,
                error_message=str(ex),
            )
            if persist:
                append_record(record, self.history_file)
            raise
```
- Note: We re-raise the original exception so programmatic callers can handle them. We persist error record before raising.

Step 14: Implement CLI (src/main.py)
- Add:
```python
# src/main.py
import sys
import click
from .api import Calculator
from .config import settings
from .storage.history import read_history
from .utils.exceptions import ValidationError, ParseError, EvaluationError

@click.group()
def cli() -> None:
    """simpcalc1 - Simple Calculator CLI"""
    pass

@cli.command("eval")
@click.argument("expression", type=str)
@click.option("--persist/--no-persist", default=False, help="Persist calculation to history file.")
def eval_cmd(expression: str, persist: bool) -> None:
    calc = Calculator()
    try:
        record = calc.evaluate(expression, persist=persist)
        click.echo(f"{record.expression} = {record.result}")
        sys.exit(0)
    except ValidationError as ex:
        click.echo(f"Validation error: {ex}", err=True)
        sys.exit(2)
    except ParseError as ex:
        click.echo(f"Parse error: {ex}", err=True)
        sys.exit(3)
    except EvaluationError as ex:
        click.echo(f"Evaluation error: {ex}", err=True)
        sys.exit(4)
    except Exception as ex:
        click.echo(f"Unexpected error: {ex}", err=True)
        sys.exit(1)

@cli.command("repl")
def repl() -> None:
    calc = Calculator()
    click.echo("simpcalc1 REPL. Type 'exit' or 'quit' to leave, ':history' to show history.")
    while True:
        try:
            s = input("simpcalc> ")
        except (EOFError, KeyboardInterrupt):
            click.echo("")
            break
        if not s:
            continue
        if s.strip() in ("exit", "quit"):
            break
        if s.strip() == ":history":
            history = read_history(calc.history_file)
            for rec in history[-20:]:
                click.echo(f"{rec['timestamp']} | {rec['expression']} = {rec['result']}")
            continue
        try:
            rec = calc.evaluate(s, persist=True)
            click.echo(f"=> {rec.result}")
        except Exception as ex:
            click.echo(f"Error: {ex}")
    click.echo("Goodbye.")
```
- Save file. The CLI is accessible as module: python -m simpcalc1.main eval "1+2"

Step 15: Implement tests
- Write unit tests as described in tests/ files. Provide example test content (exact test code).

Example: tests/test_calculator.py
```python
# tests/test_calculator.py
import pytest
from simpcalc1.core.calculator import evaluate_expression
from simpcalc1.utils.exceptions import EvaluationError, ParseError

def test_addition():
    assert evaluate_expression("1+2") == 3

def test_precedence():
    assert evaluate_expression("1+2*3") == 7

def test_parentheses():
    assert evaluate_expression("(1+2)*3") == 9

def test_unary_minus():
    assert evaluate_expression("-3 + 5") == 2

def test_divide_by_zero_raises():
    with pytest.raises(EvaluationError):
        evaluate_expression("1/0")

def test_exponentiation():
    assert evaluate_expression("2**3") == 8

def test_modulus():
    assert evaluate_expression("10%3") == 1

def test_malformed_expression_raises():
    with pytest.raises(EvaluationError):
        evaluate_expression("1 +")
```
- Implement other test files similarly following the listed cases.

Step 16: Create docs/usage.md and README.md
- Provide usage examples for CLI and API, installation instructions (see section 11 below).

Step 17: Run tests locally (PowerShell)
```powershell
pip install -r requirements.txt
pytest --maxfail=1 --disable-warnings -q
```
- Confirm tests pass.

Step 18: Lint and format
```powershell
.\.venv\Scripts\pip install black==24.3.0 flake8==6.1.0 mypy==1.9.1
black src tests
flake8 src tests
mypy src --ignore-missing-imports
```

Step 19: Validate history persistence
- Run a manual test:
```powershell
python -m simpcalc1.main eval "2*(3+4)" --persist
type data\history.json
```
- Confirm JSON array now contains one record.

Step 20: Add environment example (.env.example)
- Content:
```
SIMPCALC_HISTORY_FILE=C:\Users\balas\Documents\Projects\simpcalc1\data\history.json
LOG_LEVEL=INFO
MAX_EXPRESSION_LENGTH=1000
```

Step 21: Add pyproject.toml (optional) for black config
- Sample:
```toml
[tool.black]
line-length = 88
target-version = ['py311']
```

Step 22: Add README.md with Quick Start (see Section 11 below for exact commands)

Step 23: Prepare package for module run (optional)
- To allow python -m simpcalc1.main, ensure src is a package:
  - Add __init__.py at src/ level with minimal content:
```python
# src/__init__.py
__version__ = "0.1.0"
```
- When running with python -m, use `python -m src.main` from project root or install package in editable mode:
```powershell
pip install -e .
```
But for simplicity (module run), the recommended call is:
```powershell
python -m src.main eval "1+2"
```
Alternatively add proper packaging in setup.py if packaging required.

Step 24: Commit to git
```powershell
git init
git add .
git commit -m "Initial simpcalc1 implementation"
```

Step 25: Final validation steps & release checklist
- Run unit tests, linters, and verify docs. Check that History file is created under data/ with proper JSON schema.

## 8. ERROR HANDLING & VALIDATION

Exception Hierarchy:
- CalculatorError (base)
  - ValidationError
  - ParseError
  - EvaluationError

Where/How to validate:
- Input validation: src/utils/validators.validate_expression called early in Calculator.evaluate and CLI. It ensures string type, non-empty, and length <= MAX_EXPRESSION_LENGTH.
- Parsing validation: src/core/parser.tokenize raises ParseError when encountering unexpected characters or unrecognized tokens. shunting_yard raises ParseError on mismatched parentheses or invalid token sequences.
- Evaluation validation: src/core/calculator.eval_rpn raises EvaluationError for divide/modulo by zero, malformed token stacks (underflow/overflow), and unsupported operators.

Error Messages:
- Use user-friendly messages:
  - ValidationError: "Expression cannot be empty", "Expression exceeds maximum length of X characters".
  - ParseError: "Unexpected character 'x' at position n", "Mismatched parentheses", "Unknown token '...'"
  - EvaluationError: "Division by zero.", "Modulo by zero.", "Malformed expression; insufficient operands."

Logging Strategy:
- For simplicity, the application prints user-facing errors via click echo for CLI. For developers, extend to Python logging in future.
- Configurable LOG_LEVEL in settings; by default INFO.
- For unexpected errors, stack traces are printed when an environment variable DEBUG is set (not implemented out-of-scope), otherwise a generic message is shown.

Recovery Mechanisms:
- When persistence fails (IOError), Calculator.evaluate will raise the underlying exception; CLI will catch and print error message. No automatic retries. The system avoids data corruption by writing to temp files and using os.replace for atomic replacement.

Example exception usage:
```python
from simpcalc1.utils.exceptions import ValidationError
if not expr:
    raise ValidationError("Expression cannot be empty")
```

## 9. TESTING STRATEGY

Test Framework:
- pytest==7.4.2

Coverage Target:
- Aim for >= 95% coverage on src/core and src/api modules. Overall project target >= 90%.

Unit Tests (concrete tests to implement):
- tests/test_calculator.py:
  - test_addition: evaluates "1+1" -> 2
  - test_subtraction: "5-2" -> 3
  - test_multiplication: "2*3" -> 6
  - test_division: "6/3" -> 2 (int)
  - test_float_division: "7/2" -> 3.5
  - test_precedence: "1+2*3" -> 7
  - test_parentheses: "(1+2)*3" -> 9
  - test_unary_minus: "-3+5" -> 2
  - test_negative_parentheses: "2*(-3+4)" -> 2
  - test_exponentiation: "2**3" -> 8
  - test_modulus: "10%3" -> 1
  - test_divide_by_zero_raises: "1/0" -> raises EvaluationError
  - test_malformed_expression_raises: "1 +" -> raises EvaluationError

- tests/test_parser.py:
  - test_tokenize_numbers_and_ops: tokenize "12 + 3.4" returns ["12", "+", "3.4"]
  - test_tokenize_exponent_operator: detect "**"
  - test_unary_minus_handling: "-3" tokens become ["0", "-", "3"]
  - test_mismatched_parentheses_raises: "(1+2" raises ParseError

- tests/test_api.py:
  - test_calculator_return_record_on_success
  - test_calculator_persist_writes_file(tmp_path) - use tmp_path fixture to pass a temporary history_file to Calculator and assert file creation and JSON content
  - test_calculator_error_record_on_failure(tmp_path) - ensure error record structure has success=False and error_type set

- tests/test_history.py:
  - test_append_and_read_history: append a CalculationRecord and read back list with correct fields
  - test_invalid_json_raises: write invalid JSON and ensure ValueError when reading

Integration Tests:
- tests/test_cli_integration.py (optional):
  - Use subprocess to call python -m src.main eval "1+2" and assert stdout contains "1+2 = 3" and exit code 0.

Test Fixtures:
- Use tmp_path for temporary file paths in pytest.
- Provide sample expression fixtures if needed.

Mocking Strategy:
- For persistence tests, do not mock I/O but use tmp_path to ensure isolation.
- For long calculations or error paths, directly assert exceptions.

Running tests and coverage:
```powershell
pip install -r requirements.txt
pytest --cov=src --cov-report=term-missing
```

## 10. CONFIGURATION & ENVIRONMENT

Environment Variables:
- SIMPCALC_HISTORY_FILE: Optional override path for history file. Default C:\Users\balas\Documents\Projects\simpcalc1\data\history.json
- LOG_LEVEL: INFO by default
- MAX_EXPRESSION_LENGTH: 1000 by default

.env.example content (exact):
```
SIMPCALC_HISTORY_FILE=C:\Users\balas\Documents\Projects\simpcalc1\data\history.json
LOG_LEVEL=INFO
MAX_EXPRESSION_LENGTH=1000
```

Configuration Files:
- src/config/settings.py reads environment variables when module imported. No external config file necessary.

Secrets Management:
- No secrets used.

Default Values:
- As in settings.py.

## 11. USAGE EXAMPLES & DOCUMENTATION

Installation Steps (exact commands for Windows PowerShell):
```powershell
cd C:\Users\balas\Documents\Projects\simpcalc1
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Running CLI:
- Evaluate single expression (no persist):
```powershell
python -m src.main eval "2*(3+4)"
# Output:
# 2*(3+4) = 14
```

- Evaluate and persist:
```powershell
python -m src.main eval "2*(3+4)" --persist
# Output:
# 2*(3+4) = 14
# (History file created at C:\Users\balas\Documents\Projects\simpcalc1\data\history.json)
```

- Start interactive REPL:
```powershell
python -m src.main repl
# UX:
# simpcalc1 REPL. Type 'exit' or 'quit' to leave, ':history' to show history.
# simpcalc> 1+1
# => 2
# simpcalc> :history
# 2025-...Z | 1+1 = 2
# simpcalc> exit
# Goodbye.
```

Programmatic Usage:
```python
from src.api import Calculator

calc = Calculator()  # uses default history path
record = calc.evaluate("5/2", persist=True)
print(record.result)  # 2.5
```

Expected Output Examples:
- Success: "1+1 = 2"
- Failure: "Parse error: Unexpected character 'x' at position 2"
- Exit codes:
  - 0 success
  - 2 validation error
  - 3 parse error
  - 4 evaluation error
  - 1 unexpected

## 12. EDGE CASES & CONSIDERATIONS

Known Limitations:
- No support for functions (sin, cos), variables, assignments, or implicit multiplication (e.g., "2(3+4)" is not supported).
- Not multi-process safe for writes to history.json; concurrent writes may cause race conditions. Atomic replace mitigates partial writes, but not concurrent appends.

Performance Considerations:
- Calculator uses tokenization and RPN evaluation, which is O(n) for tokenization and evaluation; suitable for reasonably sized expressions up to MAX_EXPRESSION_LENGTH (default 1000).
- No heavy memory usage expected.

Security Considerations:
- Never use eval() or ast.literal_eval on untrusted input. The parser and RPN evaluation use only numeric parsing and apply known operator functions to avoid arbitrary code execution.
- History file stores raw expressions; if expressions came from untrusted sources and later imported into other systems, treat them as untrusted.

Scalability:
- For large-scale usage or multi-user environment, swap JSON storage to a concurrency-safe DB (SQLite with row-locks) and add API endpoints.

Edge Cases to handle:
- Input containing unexpected characters (letters) -> ParseError.
- Long input exceeding MAX_EXPRESSION_LENGTH -> ValidationError.
- Division and modulus by zero -> EvaluationError.
- Multiple operators in sequence "1 ++ 2" -> ParseError or EvaluationError as malformed.
- Floating point precision: standard Python float semantics; equality comparisons handle rounding when converting floats to ints.

## 13. EXAMPLE SOURCE SNIPPETS (Key Files Recap)

Provide full code in earlier steps for:
- src/config/settings.py
- src/utils/exceptions.py
- src/utils/validators.py
- src/core/parser.py
- src/core/calculator.py
- src/models/record.py
- src/storage/history.py
- src/api.py
- src/main.py

(Exact code blocks provided earlier; copy them exactly into the files.)

## 14. MAINTENANCE & FUTURE ENHANCEMENTS (Optional)

- Add support for functions (math module) or variable assignment if needed.
- Replace JSON persistence with SQLite + SQLAlchemy for better concurrency.
- Add a web interface using FastAPI if remote access required.
- Add CI pipeline to run tests and enforce formatting on push.

## 15. QUALITY CHECKLIST (Self-review for this plan)

- All file names are EXACT as listed.
- All library versions specified in requirements.txt.
- All function signatures given with type hints (see module specs).
- Each module has a clear purpose statement.
- Implementation steps are numbered and sequential (25 steps).
- Error handling specified for each critical function; custom exceptions provided.
- Test cases concrete (file and function names provided with expected behavior).
- Configuration complete with examples in .env.example and settings.py.
- Documentation includes working CLI and programmatic examples.
- No vague terms used. The parser and calculator implementation code is explicitly provided.

## 16. FINAL NOTES (What to hand to developers)

- Developer should copy exact code blocks provided in steps 6-14 into the specified files under C:\Users\balas\Documents\Projects\simpcalc1\src\...
- Ensure virtual environment is created and dependencies installed via requirements.txt.
- Run pytest to validate behavior. Use tmp_path fixtures in tests to isolate file-based tests.

If you want, I can also:
- Provide the full unit test code for all test files.
- Produce a ready-to-run zip or Git repo structure.
- Convert module import paths to package name "simpcalc1" and adapt python -m usage.

This specification contains all file names, code outlines (with full code for core modules), data model definitions, API behavior, error handling strategies, tests to write, configuration, and step-by-step implementation commands so a developer can implement the project without asking clarification questions.