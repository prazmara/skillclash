---
name: python-numpy-style+python-google-style
description: Merged skill that replaces `python-numpy-style` and `python-google-style`. Use for any Python function.
---

# Merged skill: python-numpy-style + python-google-style

This skill replaces `python-numpy-style` and `python-google-style`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `python-numpy-style`

- Start the module with `from __future__ import annotations`.
- State the time complexity as `Complexity: O(...)`.
- Mark each non-obvious step with a comment that starts with `# NOTE:`.

## Rules kept unchanged from `python-google-style`

- Write the docstring in Google style with `Args:` and `Returns:` sections. Never use underlined section headers.
- Reply with one Python code block and nothing outside it.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the function name in the Google style format with a verb prefix, followed by an underscore, and then the action or purpose of the function. Underline the `Parameters` section in the docstring with dashes, and avoid using `Args:`. For example: ```python def get_array_sum(arr: np.ndarray) -> float: """ Computes the sum of the elements in the given array. Parameters ---------- arr : np.ndarray The input array. Returns ------- float The sum of the elements in the input array. """ ... ```
- Write functions with the following structure: ```python def function_name(input): """Function description.""" if not isinstance(input, valid_input_type): raise ValueError("Invalid input: {}".format(input)) # Function body __all__ = ['function_name'] ```
- Write a doctest-style example using `>>>` within the docstring, adhering to the Google Python Style Guide, by including at least one usage example with a `>>>` prompt in the docstring, as follows: ``` """ Example using numpy-style: >>> import numpy as np >>> array = np.array([1, 2, 3]) >>> print(array) [1 2 3] """ ```

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
