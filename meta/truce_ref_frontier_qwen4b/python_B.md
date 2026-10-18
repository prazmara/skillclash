<skill>
---
name: python-numpy-style+python-google-style
description: Merged skill that replaces `python-numpy-style` and `python-google-style`. Use for any Python function.
---

# Merged skill: python-numpy-style + python-google-style

This skill replaces `python-numpy-style` and `python-google-style`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `python-numpy-style`

- State the time complexity as `Complexity: O(...)`.
- Export the function by defining `__all__`.
- Mark each non-obvious step with a comment that starts with `# NOTE:`.
- Write the docstring in NumPy style, with a `Parameters` header underlined by dashes. Never use `Args:`.

## Rules kept unchanged from `python-google-style`

- Name the function with a verb prefix: `get_`, `compute_`, `build_`, `parse_`, `validate_`, `find_`, `count_`, `format_`, or `to_`.
- Show a doctest-style example that uses `>>>`. Reject invalid input by raising `ValueError`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Start the module with `from __future__ import annotations`. Annotate every parameter and the return value with type hints.
- Show a doctest-style example that uses `>>>`. Reject invalid input by raising `ValueError`.
- State the time complexity in the docstring using `Complexity: O(...)`.
- For functions that validate or process input, validate input parameters and raise `ValueError` for invalid inputs (e.g., empty, out-of-range, or improperly structured data).

## Example

Request: Write a Python function that validates a password based on length and character types.

Output:

```python
from __future__ import annotations

def validate_password(password: str) -> bool:
    """
    Validate a password based on length and character types.

    Parameters
    ----------
    password : str
        The password string to validate.

    Returns
    -------
    bool
        True if the password meets the criteria, False otherwise.

    Complexity: O(n)
    Examples
    --------
    >>> validate_password("Password123")
    True
    >>> validate_password("pass")
    False
    >>> validate_password("123456")
    False
    >>> validate_password("")
    False
    """
    if not password:
        raise ValueError("Password cannot be empty.")

    # NOTE: Check minimum length requirement (at least 8 characters)
    if len(password) < 8:
        return False

    # NOTE: Check for at least one uppercase letter
    if not any(c.isupper() for c in password):
        return False

    # NOTE: Check for at least one lowercase letter
    if not any(c.islower() for c in password):
        return False

    # NOTE: Check for at least one digit
    if not any(c.isdigit() for c in password):
        return False

    # NOTE: Check for at least one special character (non-alphanumeric)
    if not any(not c.isalnum() for c in password):
        return False

    return True

__all__ = ["validate_password"]
```

Request: Write a Python function that checks if a list is sorted in ascending order.

Output:

```python
from __future__ import annotations

def is_sorted_ascending(numbers: list[int]) -> bool:
    """
    Check if a list of numbers is sorted in ascending order.

    Parameters
    ----------
    numbers : list of int
        A list of integers to check for ascending order.

    Returns
    -------
    bool
        True if the list is sorted in ascending order, False otherwise.

    Complexity: O(n)
    Examples
    --------
    >>> is_sorted_ascending([1, 2, 3, 4, 5])
    True
    >>> is_sorted_ascending([1, 3, 2, 4, 5])
    False
    >>> is_sorted_ascending([])
    True
    >>> is_sorted_ascending([5])
    True
    """
    if not numbers:
        return True

    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            return False
    return True

__all__ = ["is_sorted_ascending"]
```

Request: Write a Python function that formats a date in ISO 8601 string format.

Output:

```python
from __future__ import annotations

def format_date_iso(date_tuple: tuple[int, int, int, int, int, int, int]) -> str:
    """
    Format a date tuple into an ISO 8601 string.

    Parameters
    ----------
    date_tuple : tuple of int
        A tuple containing (year, month, day, hour, minute, second, microsecond)
        representing the date and time to be formatted.

    Returns
    -------
    str
        The date and time formatted as an ISO 8601 string (e.g., "2023-12-03T10:30:45.123456").

    Complexity: O(1)
    Examples
    --------
    >>> format_date_iso((2023, 12, 3, 10, 30, 45, 123456))
    '2023-12-03T10:30:45.123456'
    >>> format_date_iso((2020, 1, 1, 0, 0
