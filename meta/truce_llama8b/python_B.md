---
name: python-numpy-style+python-google-style
description: Merged skill that replaces `python-numpy-style` and `python-google-style`. Use for any Python function.
---

# Merged skill: python-numpy-style + python-google-style

This skill replaces `python-numpy-style` and `python-google-style`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `python-numpy-style`

- Start the module with `from __future__ import annotations`.
- Show a doctest-style example that uses `>>>`.
- State the time complexity as `Complexity: O(...)`.
- Export the function by defining `__all__`.
- Mark each non-obvious step with a comment that starts with `# NOTE:`.
- Write the docstring in NumPy style, with a `Parameters` header underlined by dashes. Never use `Args:`.

## Rules kept unchanged from `python-google-style`

- Name the function with a verb prefix: `get_`, `compute_`, `build_`, `parse_`, `validate_`, `find_`, `count_`, `format_` or `to_`.
- Write the docstring in Google style with `Args:` and `Returns:` sections. Never use underlined section headers.
- Annotate every parameter and the return value with type hints.
- Reject invalid input by raising `ValueError`.
- Include at least one usage example with a `>>>` prompt in the docstring.
- Reply with one Python code block and nothing outside it.

## Example

Request: Write a Python function that returns the median of a list of numbers.

Output:

```
from __future__ import annotations
import numpy as np

def get_median(numbers: list[float]) -> float:
    """
    Returns the median of a list of numbers.

    Args:
        numbers: A list of numbers.

    Returns:
        The median of the input list.

    Raises:
        ValueError: If the input list is empty.

    >>> get_median([1, 3, 5])
    3.0
    >>> get_median([1, 2, 3, 4])
    2.5
    """
    # NOTE: Check if the input list is empty
    if not numbers:
        raise ValueError("Input list is empty")

    # NOTE: Sort the input list in ascending order
    numbers.sort()

    # NOTE: Calculate the median
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2

__all__ = ["get_median"]
```
