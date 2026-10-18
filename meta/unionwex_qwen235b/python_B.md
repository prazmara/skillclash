---
name: python-numpy-style+python-google-style
description: Combined rules of `python-numpy-style` and `python-google-style`. Use for any Python function.
---

# Combined skill: python-numpy-style + python-google-style

Follow every rule below.

## Rules from `python-numpy-style`

- Start the module with `from __future__ import annotations`.
- Show a doctest-style example that uses `>>>`.
- State the time complexity as `Complexity: O(...)`.
- Export the function by defining `__all__`.
- Mark each non-obvious step with a comment that starts with `# NOTE:`.
- Write the docstring in NumPy style, with a `Parameters` header underlined by dashes. Never use `Args:`.

## Rules from `python-google-style`

- Name the function with a verb prefix: `get_`, `compute_`, `build_`, `parse_`, `validate_`, `find_`, `count_`, `format_` or `to_`.
- Write the docstring in Google style with `Args:` and `Returns:` sections. Never use underlined section headers.
- Annotate every parameter and the return value with type hints.
- Reject invalid input by raising `ValueError`.
- Include at least one usage example with a `>>>` prompt in the docstring.
- Reply with one Python code block and nothing outside it.

If two rules cannot both hold, the rule from `python-numpy-style` wins.

## Example

Request: Write a Python function that returns the median of a list of numbers.

Output:

```python
from __future__ import annotations

__all__ = ["get_median"]

def get_median(numbers: list[float] | list[int]) -> float:
    """Return the median of a list of numbers.
    
    Parameters
    ----------
    numbers : list[float] | list[int]
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
    >>> get_median([1, 3, 3, 6, 7, 8, 9])
    6
    >>> get_median([1, 2, 3, 4, 5, 6])
    3.5
    
    Complexity: O(n log n)
    """
    if not numbers:
        raise ValueError("Cannot compute median of an empty list.")
    
    # NOTE: Sort the list to find the middle element(s)
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    # NOTE: If odd, return the middle element; if even, return average of two middle elements
    if n % 2 == 1:
        return float(sorted_numbers[n // 2])
    else:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2.0
```
