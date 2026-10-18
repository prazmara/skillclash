---
name: python-google-style+python-numpy-style
description: Merged skill that replaces `python-google-style` and `python-numpy-style`. Use for any Python function.
---

# Merged skill: python-google-style + python-numpy-style

This skill replaces `python-google-style` and `python-numpy-style`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `python-google-style`

- Write the docstring in Google style with `Args:` and `Returns:` sections. Never use underlined section headers.
- Annotate every parameter and the return value with type hints.
- Reply with one Python code block and nothing outside it.

## Rules kept unchanged from `python-numpy-style`

- State the time complexity as `Complexity: O(...)`.
- Mark each non-obvious step with a comment that starts with `# NOTE:`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the function name with a verb prefix (e.g., `get_`, `compute_`, `build_`, `parse_`, `validate_`, `find_`, `count_`, `format_`, or `to_`) and document it in NumPy style, using a `Parameters` header underlined by dashes, as follows: ``` def get_data(parameters: dict): """ Description of the function. Parameters ---------- parameters : dict Description of the parameters. Returns ------- result : Any Description of the result. """ ```
- Write functions with the following structure: ```python def function_name(valid_input): # Function body __all__ = ['function_name'] ``` In case of invalid input, raise `ValueError`: ```python def function_name(valid_input): if not isinstance(valid_input, (list, dict, str, int, float)): raise ValueError("Invalid input type. Expected one of: list, dict, str, int, float.") # Function body __all__ = ['function_name'] ```
- Write a docstring that includes an example of usage with a `>>>` prompt, followed by a doctest-style example using `>>>`, separated by a blank line. For instance: ``` """ Usage: my_function(arg1, arg2) Tests: >>> result = my_function(1, 2) >>> assert result == 3 """ ```

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
