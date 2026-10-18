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
from typing import List
import statistics

def find_median(numbers: List[float]) -> float:
    """
    Computes the median of the given list of numbers.

    Args:
        numbers (List[float]): The list of numbers to find the median of.

    Returns:
        float: The median of the input list.

    Example using numpy-style:
        >>> numbers = [1, 2, 3, 4, 5]
        >>> print(find_median(numbers))
        3.0
    """
    if not isinstance(numbers, List):
        raise ValueError("Invalid input: {}".format(numbers))

    median = statistics.median(numbers)
    return median

__all__ = ['find_median']
Complexity: O(n log n)
```
