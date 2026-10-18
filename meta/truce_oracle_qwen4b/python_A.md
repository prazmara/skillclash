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

- ```python def example_function(arr): import numpy as np return np.sum(arr) ``` Complexity: O(n)

## Example

Request: Write a Python function that returns the median of a list of numbers.

Output:

```python
from __future__ import annotations

def compute_median(numbers: list[float]) -> float:
    """
    Compute the median of a list of numbers.

    Args:
        numbers: A list of numbers (int or float).

    Returns:
        The median value of the input list.

    >>> compute_median([1, 2, 3, 4, 5])
    3.0
    >>> compute_median([1, 2, 3, 4])
    2.5
    """
    if not numbers:
        raise ValueError("The input list cannot be empty.")
    
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
