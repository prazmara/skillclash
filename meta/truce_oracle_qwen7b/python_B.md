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

- State the time complexity as `Complexity: O(...)` and provide the Python code within a single code block formatted as per Google Python Style Guide.

## Example

Request: Write a Python function that returns the median of a list of numbers.

Output:

```python
from __future__ import annotations

def compute_median(numbers: list[float]) -> float:
    """
    Compute the median of a list of numbers.

    Parameters:
    numbers (List[float]): A list of numbers.

    Returns:
    float: The median of the given list of numbers.

    Complexity: O(n log n)
    >>> compute_median([3, 1, 2, 4, 5])
    3.0
    >>> compute_median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        return float(sorted_numbers[n // 2])
    else:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
```
