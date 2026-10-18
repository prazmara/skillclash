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

```
from __future__ import annotations

def compute_median(numbers: list[float]) -> float:
    """
    Compute the median of a list of numbers.

    Parameters
    ----------
    numbers : list of float
        A list of numbers for which the median is to be computed.

    Returns
    -------
    float
        The median value of the input list.

    Examples
    --------
    >>> compute_median([1, 2, 3, 4, 5])
    3.0
    >>> compute_median([1, 3, 3, 6, 7, 8, 9])
    6.0
    >>> compute_median([5])
    5.0
    """
    if not numbers:
        raise ValueError("The list of numbers is empty.")

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 1:
        # Odd number of elements: return the middle element
        return float(sorted_numbers[n // 2])
    else:
        # Even number of elements: return the average of the two middle elements
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2.0

__all__ = ["compute_median"]
```
