"""
Tokenizer and shunting-yard implementation for simpcalc1.

This module provides a safe tokenizer that recognizes numbers (integers and decimals),
operators (+, -, *, /, %, **), and parentheses. It also converts token lists to
Reverse Polish Notation (RPN) using the Shunting-yard algorithm.

All errors raise ParseError from src.utils.exceptions.
"""
from typing import List

from ..utils.exceptions import ParseError

_OPERATORS = {"+", "-", "*", "/", "%", "**"}
_WHITESPACE = set(" \t\n\r")


def tokenize(expression: str) -> List[str]:
    """Break expression into tokens: numbers, operators, parentheses.

    Returns a list of tokens in order. Raises ParseError on unexpected characters.
    """
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
        if ch == '*' and i + 1 < n and expression[i + 1] == '*':
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
    """Convert tokens to Reverse Polish Notation (RPN) using the Shunting-yard algorithm.

    Returns RPN token list. Raises ParseError on mismatched parentheses or invalid syntax.
    """
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
                while (
                    stack
                    and stack[-1] not in ('(')
                    and (
                        (_precedence(stack[-1]) > _precedence(token))
                        or (_precedence(stack[-1]) == _precedence(token) and token != '**')
                    )
                ):
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
