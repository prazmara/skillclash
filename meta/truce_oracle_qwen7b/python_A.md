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

- Reply with one Python code block and state the time complexity as `Complexity: O(...)` below the code block.

## Example

Request: Write a Python function that returns the median of a list of numbers.

Output:

```python
from __future__ import annotations

def compute_median(numbers: list[float]) -> float:
    """
    Compute the median of a list of numbers.

    Args:
        numbers: A list of floats representing the numbers.

    Returns:
        The median of the given numbers.

    >>> compute_median([1.0, 2.0, 3.0])
    2.0
    >>> compute_median([1.0, 2.0, 3.0, 4.0])
    2.5
    """
    if not numbers:
        raise ValueError("The list of numbers is empty.")
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

__all__ = ['compute_median']
```
Complexity: O(n log n)
