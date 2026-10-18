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

- To satisfy both rules, write a Python code block that performs a task using numpy, and state the time complexity in the format `Complexity: O(...)` within the code block. For example: ```python import numpy as np def matrix_multiply(A, B): C = np.dot(A, B) return C # Complexity: O(n^3) for matrix multiplication using numpy's dot function ``` This code block uses numpy for matrix multiplication and includes the time complexity statement as required by both styles.

## Example

Request: Write a Python function that returns the median of a list of numbers.

Output:

```python
from __future__ import annotations
from typing import List
import numpy as np

def compute_median(numbers: List[float]) -> float:
    """
    Compute the median of a list of numbers.

    Args:
    numbers (List[float]): A list of numbers.

    Returns:
    float: The median of the list.

    >>> compute_median([1, 3, 3, 6, 7, 8, 9])
    6.0

    Complexity: O(n) for sorting the list and finding the median.
    """
    sorted_numbers = np.sort(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2.0
    else:
        return sorted_numbers[mid]

__all__ = ['compute_median']
```
