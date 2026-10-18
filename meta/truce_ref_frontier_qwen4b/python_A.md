<skill>
---
name: python-google-style+python-numpy-style
description: Merged skill that replaces `python-google-style` and `python-numpy-style`. Use for any Python function.
---

# Merged skill: python-google-style + python-numpy-style

This skill replaces `python-google-style` and `python-numpy-style`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `python-google-style`

- Name the function with a verb prefix: `get_`, `compute_`, `build_`, `parse_`, `validate_`, `find_`, `count_`, `format_`, or `to_`.
- Write the docstring in Google style with `Args:` and `Returns:` sections. Never use underlined section headers.
- Reject invalid input by raising `ValueError`.
- Include at least one usage example with a `>>>` prompt in the docstring.
- Reply with one Python code block and nothing outside it.

## Rules kept unchanged from `python-numpy-style`

- State the time complexity as `Complexity: O(...)`.
- Export the function by defining `__all__`.
- Mark each non-obvious step with a comment that starts with `# NOTE:`.
- Write the docstring in NumPy style, with a `Parameters` header underlined by dashes. Never use `Args:`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Annotate every parameter and the return value with type hints. Start the module with `from __future__ import annotations`.

## Conflict resolution and enforcement

The original rules from `python-google-style` and `python-numpy-style` conflict in docstring formatting:
- Google style requires `Args:` and `Returns:` sections without underlining.
- NumPy style requires `Parameters` and `Returns` sections underlined by dashes.

**Resolution**: These are mutually incompatible. Therefore, we **must** choose one consistent format. However, the requirement to satisfy *both* Google and NumPy style rules cannot be fully met without violating one.

Thus, we **replace** the Google-style docstring rule with the **NumPy style** because:
- It is more comprehensive and aligned with modern Python documentation standards (e.g., in NumPy, SciPy, and PyTorch).
- The underlined section headers (`----------`) are standard and explicit.
- The Google-style `Args:` and `Returns:` headers are ambiguous and inconsistent with modern best practices.

**Final docstring format**:
- Use **NumPy style** with:
  - `Parameters` section underlined by `----------`
  - `Returns` section underlined by `----------`
- Never use `Args:` or `Returns:` headers.
- Include a usage example with `>>>` in the docstring.

> ⚠️ The rule "Write the docstring in Google style with `Args:` and `Returns:` sections" is **replaced** by the NumPy style docstring format due to incompatibility. This change ensures full compliance with all other rules.

## Time Complexity Requirement

Each function must include a `Complexity: O(...)` line in the docstring, clearly stating the time complexity.

## Function Naming

All functions must begin with one of the verb prefixes: `get_`, `compute_`, `build_`, `parse_`, `validate_`, `find_`, `count_`, `format_`, or `to_`.

## Input Validation

All functions must reject invalid input by raising a `ValueError` with a clear message. This includes invalid types, empty inputs, or out-of-range values.

## Type Hints and Future Import

Start the module with `from __future__ import annotations`. Annotate all parameters and return values with proper type hints.

## Export

All exported functions must be included in the `__all__` list.

## Mark Non-Obvious Steps

Each non-obvious step in the function logic must be accompanied by a comment that starts with `# NOTE:`.

## Example: Format a date in ISO 8601 string format

```python
from __future__ import annotations
from datetime import datetime

def format_date_iso8601(date_obj: datetime) -> str:
    """
    Format a datetime object into an ISO 8601 string.

    Parameters
    ----------
    date_obj : datetime
        The datetime object to format.

    Returns
    -------
    str
        The ISO 8601 formatted string representation of the datetime.

    Examples
    --------
    >>> format_date_iso8601(datetime(2023, 10, 5, 14, 30, 0))
    '2023-10-05T14:30:00'

    Complexity: O(1)
    """
    if not isinstance(date_obj, datetime):
        raise ValueError("Input must be a datetime object.")
    
    return date_obj.isoformat()

__all__ = ["format_date_iso8601"]
```

## Example: Check if a number is a perfect square

```python
from __future__ import annotations

def compute_perfect_square(number: int) -> bool:
    """
    Check if a number is a perfect square.

    Parameters
    ----------
    number : int
        The number to check if it is a perfect square.

    Returns
    -------
    bool
        True if the number is a perfect square, False otherwise.

    Examples
    --------
    >>> compute_perfect_square(16)
    True
    >>> compute_perfect_square(14)
    False

    Complexity: O(1)
    """
    if number < 0:
        raise ValueError("Perfect
