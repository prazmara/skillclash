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

- Write a single Python code block, enclosed in triple quotes (``` ... ```). Include the time complexity at the beginning of the code block, prefixed with `Complexity: O(...)`, followed by a newline. Use the appropriate style from the `python-google-style` and `python-numpy-style` for the rest of the code. Example: ``` Complexity: O(n) def my_function(input_list): # Your code here pass ```

## Example

Request: Write a Python function that returns the median of a list of numbers.

Output:

```python
from __future__ import annotations

import typing
from typing import List

Complexity: O(n * log(n))

def find_median(numbers: List[float]) -> float:
    """
    Computes the median of a list of numbers.

    Args:
        numbers (List[float]): The list of numbers to find the median of.

    Returns:
        float: The median of the input list.

    Raises:
        ValueError: If the input list is empty.

    Example:
        >>> find_median([1, 2, 3, 4, 5])
        3.0
        >>> find_median([1, 2, 3])
        2.0
        >>> find_median([])
        Raises ValueError: list is empty
    """

    if not numbers:
        raise ValueError("list is empty")

    numbers.sort()
    n = len(numbers)

    if n % 2 == 0:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else:
        return numbers[n // 2]
```
