"""
Calculator engine: evaluates expressions by converting to RPN and computing result.

Public functions:
- eval_rpn(rpn_tokens: List[str]) -> Union[int, float]
- evaluate_expression(expression: str) -> Union[int, float]

Raises EvaluationError on evaluation issues.
"""
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
    """Evaluate RPN tokens and return numeric result (int or float).

    Raises:
        EvaluationError: For divide by zero, stack underflow, invalid operations.
    """
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
    """Full pipeline: tokenize -> shunting-yard -> eval_rpn -> return numeric result.

    Raises:
        ParseError, EvaluationError
    """
    tokens = tokenize(expression)
    rpn = shunting_yard(tokens)
    return eval_rpn(rpn)
