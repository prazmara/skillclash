---
name: python-numpy-style+python-google-style
description: Merged skill that replaces `python-numpy-style` and `python-google-style`. Use for any Python function.
---

# Merged skill: python-numpy-style + python-google-style

This skill replaces `python-numpy-style` and `python-google-style`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `python-numpy-style`

- Write the docstring in NumPy style, with a `Parameters` header underlined by dashes. Never use `Args:`.
- Start the module with `from __future__ import annotations`.
- Mark each non-obvious step with a comment that starts with `# NOTE:`.
- Export the function by defining `__all__`.
- Show a doctest-style example that uses `>>>`.

## Rules kept unchanged from `python-google-style`

- Annotate every parameter and the return value with type hints.
- Reject invalid input by raising `ValueError`.
- Name the function with a verb prefix: `get_`, `compute_`, `build_`, `parse_`, `validate_`, `find_`, `count_`, `format_` or `to_`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- "State the time complexity as `Complexity: O(...)` and reply with one Python code block and nothing outside it."

## Example

Request: Write a Python function that returns the median of a list of numbers.

Output:

```python
from typing import List

def compute_median(numbers: List[float]) -> float:
    """
    Calculate the median of a list of numbers.

    Parameters
    ----------
    numbers : List[float]
        A list of numbers to calculate the median of.

    Returns
    -------
    float
        The median of the list of numbers.

    Examples
    --------
    >>> compute_median([1, 3, 3, 6, 7, 8, 9])
    6.0
    """
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2.0
    else:
        return numbers[mid]

# NOTE: The time complexity of this function is O(n log n) due to the sort operation.
```
