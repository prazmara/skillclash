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

- Write a single Python code block that includes the time complexity in a comment, following the format `Complexity: O(...)`, and do not include any text outside the code block.

## Example

Request: Write a Python function that returns the median of a list of numbers.

Output:

```
from __future__ import annotations
__all__ = ['get_median']

def get_median(numbers: list[float]) -> float:
    """
    Returns the median of a list of numbers.

    Parameters
    ----------
    - numbers: list[float]
        A list of numbers.

    Returns
    -------
    float
        The median of the input list.

    Raises
    ------
    ValueError
        If the input list is empty.

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

    # NOTE: Calculate the length of the input list
    n = len(numbers)

    # NOTE: If the length of the input list is odd, return the middle element
    if n % 2 == 1:
        return numbers[n // 2]
    # NOTE: If the length of the input list is even, return the average of the two middle elements
    else:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2

Complexity: O(n log n)
```
