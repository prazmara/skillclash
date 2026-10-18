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
def compute_median(numbers: list) -> float:
    """
    Parameters
    ----------
    numbers : list of int or float
        A list of numbers.

    Returns
    -------
    float
        The median of the given list of numbers.

    Complexity: O(n log n)

    >>> compute_median([3, 1, 2, 4, 5])
    3.0
    >>> compute_median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

__all__ = ['compute_median']
```
