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
def get_median(numbers: list) -> float:
    """
    Computes the median of a list of numbers.

    Parameters
    ----------
    numbers : list
        A sorted list of numbers.

    Returns
    -------
    median : float
        The middle value of the list. If the list has an odd length, the middle value is returned.
        If the list has an even length, the average of the two middle values is returned.

    Examples
    --------
    >>> get_median([1, 2, 3, 4])
    2.5
    >>> get_median([1, 2, 3])
    2.0
    >>> get_median([1, 2])
    1.5
    """
    if not isinstance(numbers, list):
        raise ValueError("Invalid input type. Expected list.")

    numbers.sort()
    length = len(numbers)

    if length == 0:
        raise ValueError("List is empty.")

    if length % 2 == 0:
        return (numbers[length // 2 - 1] + numbers[length // 2]) / 2
    else:
        return numbers[length // 2]

    __all__ = ['get_median']
    Complexity: O(n log n)
    # NOTE: The sorting operation has a time complexity of O(n log n) in the worst case.
```
