---
name: python-google-style+python-numpy-style
description: Merged skill that replaces `python-google-style` and `python-numpy-style`. Use for any Python function.
---

# Merged skill: python-google-style + python-numpy-style

This skill replaces `python-google-style` and `python-numpy-style`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `python-google-style`

- Reply with one Python code block and nothing outside it.

## Rules kept unchanged from `python-numpy-style`

- Mark each non-obvious step with a comment that starts with `# NOTE:`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- To satisfy both the `python-google-style` and `python-numpy-style` rules, name your function with a verb prefix like `get_`, `compute_`, etc., and start your module with `from __future__ import annotations`. Ensure the function name and module start statement are correctly placed in your code.
- Write the docstring in Google style with `Args:` and `Returns:` sections, and underlined `Parameters` header by dashes for NumPy style.
- Annotate every parameter and the return value with type hints (python-google-style) and state the time complexity as `Complexity: O(...)` (python-numpy-style).
- To satisfy both rules, define a function that raises a `ValueError` for invalid input and includes an `__all__` list with the function's name. For example: ```python __all__ = ['my_function'] def my_function(x): if not isinstance(x, (int, float)): raise ValueError("Invalid input: x must be an int or float") # Function implementation here ```
- Include a docstring with a `>>>` prompt and a doctest-style example using `>>>` in the same output. For example: ```python def add(a, b): """ Adds two numbers together. >>> add(2, 3) 5 """ return a + b ```

## Example

Request: Write a Python function that returns the median of a list of numbers.

Output:

```python
from __future__ import annotations
from typing import List

def compute_median(numbers: List[float]) -> float:
    """
    Computes the median of a list of numbers.

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        float: The median of the list.

    >>> compute_median([1, 3, 3, 6, 7, 8, 9])
    6
    """
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2.0
    else:
        return numbers[mid]

__all__ = ['compute_median']
```
