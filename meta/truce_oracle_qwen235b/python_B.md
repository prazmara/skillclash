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

- Reply with one Python code block and nothing outside it. State the time complexity as `Complexity: O(...)`.

## Example

Request: Write a Python function that returns the median of a list of numbers.

Output:

```python
from __future__ import annotations


def compute_median(numbers: list[float]) -> float:
    """Compute the median of a list of numbers.

    Parameters
    ----------
    numbers : list[float]
        A non-empty list of numbers.

    Returns
    -------
    float
        The median value.

    Raises
    ------
    ValueError
        If the input list is empty.

    Examples
    --------
    >>> compute_median([1, 2, 3])
    2
    >>> compute_median([1, 2, 3, 4])
    2.5
    """
    if not numbers:
        raise ValueError("Cannot compute median of an empty list.")
    
    # NOTE: Sort the list to find the middle value(s)
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    # NOTE: If odd, return the middle element; if even, return average of two middle elements
    if n % 2 == 1:
        return float(sorted_numbers[n // 2])
    else:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2.0


__all__ = ["compute_median"]
# Complexity: O(n log n)
```
