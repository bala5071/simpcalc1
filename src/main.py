"""
Command-line interface for simpcalc1 using click.
Provides two commands:
- eval <expression> [--persist]
- repl (interactive prompt)
"""
import sys
import click
from .api import Calculator
from .config import settings
from .storage.history import read_history
from .utils.exceptions import ValidationError, ParseError, EvaluationError


@click.group()
def cli() -> None:
    """simpcalc1 - Simple Calculator CLI"""


@cli.command("eval")
@click.argument("expression", type=str)
@click.option("--persist/--no-persist", default=False, help="Persist calculation to history file.")
def eval_cmd(expression: str, persist: bool) -> None:
    """Evaluate a single expression and print the result."""
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
    """Start an interactive REPL for evaluating expressions."""
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
            try:
                history = read_history(calc.history_file)
                if not history:
                    click.echo("No history found. Use --persist to save calculations.")
                else:
                    # history is a list of CalculationRecord objects or dicts
                    # The storage.read_history returns CalculationRecord instances
                    for rec in history[-20:]:
                        # rec may be CalculationRecord instance
                        if hasattr(rec, "timestamp"):
                            click.echo(f"{rec.timestamp} | {rec.expression} = {rec.result}")
                        else:
                            # fallback if dict
                            click.echo(f"{rec.get('timestamp')} | {rec.get('expression')} = {rec.get('result')}")
            except Exception as ex:
                click.echo(f"Error reading history: {ex}")
            continue
        try:
            rec = calc.evaluate(s, persist=True)
            click.echo(f"=> {rec.result}")
        except Exception as ex:
            click.echo(f"Error: {ex}")
    click.echo("Goodbye.")


if __name__ == "__main__":
    cli()
