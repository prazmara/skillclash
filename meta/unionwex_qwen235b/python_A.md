---
name: python-google-style+python-numpy-style
description: Combined rules of `python-google-style` and `python-numpy-style`. Use for any Python function.
---

# Combined skill: python-google-style + python-numpy-style

Follow every rule below.

## Rules from `python-google-style`

- Name the function with a verb prefix: `get_`, `compute_`, `build_`, `parse_`, `validate_`, `find_`, `count_`, `format_` or `to_`.
- Write the docstring in Google style with `Args:` and `Returns:` sections. Never use underlined section headers.
- Annotate every parameter and the return value with type hints.
- Reject invalid input by raising `ValueError`.
- Include at least one usage example with a `>>>` prompt in the docstring.
- Reply with one Python code block and nothing outside it.

## Rules from `python-numpy-style`

- Start the module with `from __future__ import annotations`.
- Show a doctest-style example that uses `>>>`.
- State the time complexity as `Complexity: O(...)`.
- Export the function by defining `__all__`.
- Mark each non-obvious step with a comment that starts with `# NOTE:`.
- Write the docstring in NumPy style, with a `Parameters` header underlined by dashes. Never use `Args:`.

If two rules cannot both hold, the rule from `python-google-style` wins.

## Example

Request: Write a Python function that returns the median of a list of numbers.

Output:

```python
from __future__ import annotations


def get_median(numbers: list[float | int]) -> float:
    """Return the median of a list of numbers.

    Args:
        numbers: A list of numeric values.

    Returns:
        The median value as a float. If the list has an odd number of elements,
        returns the middle element. If even, returns the average of the two middle elements.

    Raises:
        ValueError: If the input list is empty.

    Examples:
        >>> get_median([1, 3, 5])
        3
        >>> get_median([1, 2, 3, 4])
        2.5
        >>> get_median([7])
        7

    Complexity: O(n log n)
    """
    if not numbers:
        raise ValueError("Cannot compute median of an empty list")

    # NOTE: Sorting is required to find the middle element(s)
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2

    # NOTE: For odd length, median is the middle element
    if n % 2 == 1:
        return float(sorted_numbers[mid])

    # NOTE: For even length, median is the average of two middle elements
    return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2.0


__all__ = []
```
