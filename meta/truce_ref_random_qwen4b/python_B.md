```xml
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
- Reject invalid input by raising `ValueError`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Start the module with `from __future__ import annotations`. Annotate every parameter and the return value with type hints.
- Show a doctest-style example that uses `>>>`. Reject invalid input by raising `ValueError`.

## Additional rule (to resolve conflicts and ensure all rules are satisfied)

- State the time complexity in the docstring using the format `Complexity: O(...)`. This must be included in the docstring after the `Returns` section.

## Fixed rule: Clarify and enforce consistent handling of input validation

- If a function requires input validation (e.g., type, value, structure), **invalid inputs must raise a `ValueError`**, not return `False` or early-exit with a conditional. This ensures that any input that fails the criteria results in a clear, unambiguous error, aligning with `python-google-style`.

> This rule explicitly replaces any pattern where a function returns `False` on invalid input (e.g., in the email validation example) with a `ValueError` raise. For example, if the input is empty, malformed, or of the wrong type, a `ValueError` must be raised — not a conditional return.

## New rule: Enforce explicit marking of non-obvious steps

- Mark each non-obvious step with a comment that starts with `# NOTE:`. This applies to any logical step that is not immediately obvious from the code (e.g., algorithmic logic, mathematical formulas, or conditional behavior that requires explanation).

## Example 1: Write a Python function that calculates the factorial of a non-negative integer.

Output:

```python
from __future__ import annotations

def compute_factorial(n: int) -> int:
    """
    Compute the factorial of a non-negative integer.

    Parameters
    ----------
    n : int
        The non-negative integer for which to compute the factorial.

    Returns
    -------
    int
        The factorial of n, defined as n! = n * (n-1) * ... * 2 * 1.

    Complexity: O(n)
    Examples
    --------
    >>> compute_factorial(0)
    1
    >>> compute_factorial(5)
    120
    >>> compute_factorial(3)
    6
    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    # NOTE: Base case: 0! and 1! are both defined as 1.
    if n == 0 or n == 1:
        return 1
    
    # NOTE: Iteratively multiply from 2 to n to compute the factorial.
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result

__all__ = ["compute_factorial"]
```

## Example 2: Write a Python function that validates a password based on length and character types.

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
    >>> validate_password("12345")
    False
    >>> validate_password("Pass!@#")
    True
    """
    if not isinstance(password, str):
        raise ValueError("Password must be a string.")
    
    # NOTE: Password must be at least 8 characters long.
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")
    
    # NOTE: Must contain at least one uppercase letter.
    if not any(c.isupper() for c in password):
        raise ValueError("Password must contain at least one uppercase letter.")
    
    # NOTE: Must contain at least one lowercase letter.
    if not any(c.islower() for c in password):
        raise ValueError("Password must contain at least one lowercase letter.")
    
    # NOTE: Must contain at least one digit.
    if not any(c.isdigit() for c in password):
        raise ValueError("Password must contain at least one digit.")
    
    # NOTE: Must contain at least one special character.
    if not any(c
