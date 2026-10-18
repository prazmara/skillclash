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

- Reply with one Python code block and nothing outside it, and inside the code block, state the time complexity as `Complexity: O(...)`.

## Example

Request: Write a Python function that returns the median of a list of numbers.

Output:

```python
from __future__ import annotations

__all__ = ['get_median']

def get_median(numbers: list[float]) -> float:
    """Return the median of a list of numbers.

    Args:
        numbers (list[float]): The list of numbers.

    Returns:
        float: The median value.

    Raises:
        ValueError: If the input list is empty.

    Examples:
        >>> get_median([1, 3, 2])
        2.0
        >>> get_median([1, 2, 3, 4])
        2.5
    """
    if not numbers:
        raise ValueError("Input list must not be empty.")
    # NOTE: Sort the list to find the median
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 1:
        # NOTE: Odd number of elements, return the middle one
        return float(sorted_numbers[mid])
    else:
        # NOTE: Even number of elements, return the average of the two middle ones
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2.0

# Complexity: O(n log n)
```
