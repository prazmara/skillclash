---
name: python-google-style+python-numpy-style
description: Merged skill that replaces `python-google-style` and `python-numpy-style`. Use for any Python function.
---

# Merged skill: python-google-style + python-numpy-style

This skill replaces `python-google-style` and `python-numpy-style`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `python-google-style`

- Write the docstring in Google style with `Args:` and `Returns:` sections. Never use underlined section headers.
- Annotate every parameter and the return value with type hints.
- Reject invalid input by raising `ValueError`.
- Name the function with a verb prefix: `get_`, `compute_`, `build_`, `parse_`, `validate_`, `find_`, `count_`, `format_` or `to_`.
- Include at least one usage example with a `>>>` prompt in the docstring.

## Rules kept unchanged from `python-numpy-style`

- Start the module with `from __future__ import annotations`.
- Mark each non-obvious step with a comment that starts with `# NOTE:`.
- Export the function by defining `__all__`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- **Combined Rule:** Write a Python code block that starts with the time complexity on the first line, followed by a colon and the complexity in parentheses, and then the code on the next line, indented with four spaces.

## Example

Request: Write a Python function that returns the median of a list of numbers.

Output:

```
from __future__ import annotations
__all__ = ['median']

def median(numbers: list[float]) -> float:
    """
    Compute the median of a list of numbers.

    Args:
        numbers: A list of numbers.

    Returns:
        The median of the input list.

    Raises:
        ValueError: If the input list is empty.

    >>> median([1, 3, 5])
    3.0
    >>> median([1, 2, 3, 4])
    2.5
    """
    # NOTE: Sort the list in ascending order
    numbers.sort()
    n = len(numbers)
    if n == 0:
        raise ValueError("Cannot compute median of an empty list")
    # NOTE: If the list has an odd length, the median is the middle element
    if n % 2 == 1:
        return numbers[n // 2]
    # NOTE: If the list has an even length, the median is the average of the two middle elements
    else:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2
```
