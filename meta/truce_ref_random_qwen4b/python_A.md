<skill>
---
name: python-google-style+python-numpy-style
description: Merged skill that replaces `python-google-style` and `python-numpy-style`. Use for any Python function. Follow every rule strictly.

# Merged skill: python-google-style + python-numpy-style

This skill replaces `python-google-style` and `python-numpy-style`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `python-google-style`
- Name the function with a verb prefix: `get_`, `compute_`, `build_`, `parse_`, `validate_`, `find_`, `count_`, `format_`, or `to_`.
- Write the docstring in Google style with `Args:` and `Returns:` sections. Never use underlined section headers.
- Reject invalid input by raising `ValueError`.
- Include at least one usage example with a `>>>` prompt in the docstring.
- Reply with one Python code block and nothing outside it.

## Rules kept unchanged from `python-numpy-style`
- State the time complexity as `Complexity: O(...)`.
- Export the function by defining `__all__`.
- Mark each non-obvious step with a comment that starts with `# NOTE:`.

## Reconciled rules (each one satisfies a rule of both skills at once)
- Annotate every parameter and the return value with type hints. Start the module with `from __future__ import annotations`.

## Resolution of conflicting rules
The use of underlined section headers (as in NumPy style) is explicitly forbidden by Google style. Therefore, **NumPy-style underlined headers are not allowed**.  
However, to satisfy both styles, we **retain the requirement for `Args:` and `Returns:`** as in Google style, and **preserve the requirement for `# NOTE:` comments** on non-obvious steps.  
The requirement to state time complexity is preserved as a separate, non-conflicting rule.  
The requirement to raise `ValueError` for invalid input is preserved as a strict rule.  
Thus, all rules are reconciled without contradiction by:
- **Using Google-style docstrings** with `Args:` and `Returns:` (no underlined headers).
- **Including a `Complexity: O(...)` line** in the docstring, placed after the `Returns:` section or as a standalone line.
- **Using `# NOTE:` comments** for any non-obvious or non-trivial logic steps.
- **Raising `ValueError`** for invalid inputs (not returning `False` or `None` for invalid inputs).

## Final Unified Rules (all satisfied)
- Name the function with a verb prefix: `get_`, `compute_`, `build_`, `parse_`, `validate_`, `find_`, `count_`, `format_`, or `to_`.
- Write the docstring in Google style with `Args:` and `Returns:` sections. Never use underlined section headers.
- Reject invalid input by raising `ValueError`.
- Include at least one usage example with a `>>>` prompt in the docstring.
- Annotate every parameter and the return value with type hints. Start the module with `from __future__ import annotations`.
- State the time complexity as `Complexity: O(...)`.
- Export the function by defining `__all__`.
- Mark each non-obvious step with a comment that starts with `# NOTE:`.

## Example

Request: Write a Python function that checks if a string is a valid email address.

Output:

```python
from __future__ import annotations

def validate_email(email: str) -> bool:
    """
    Validate if a string is a valid email address.

    Args:
        email: The string to validate as an email address.

    Returns:
        True if the string is a valid email address, False otherwise.

    Examples:
        >>> validate_email("user@example.com")
        True
        >>> validate_email("invalid.email")
        False

    Complexity: O(n)
    """
    # NOTE: Check if the email is empty or None
    if not email or not isinstance(email, str):
        raise ValueError("Email must be a non-empty string.")

    # NOTE: Check if the email contains exactly one '@' symbol
    if email.count('@') != 1:
        raise ValueError("Email must contain exactly one '@' symbol.")

    # NOTE: Split the email into local and domain parts
    local, domain = email.rsplit('@', 1)

    # NOTE: Check if both local and domain parts are non-empty
    if not local or not domain:
        raise ValueError("Email must have both local and domain parts.")

    # NOTE: Check if the domain contains at least one dot and does not start or end with a dot
    if '.' not in domain or domain.startswith('.') or domain.endswith('.'):
        raise ValueError("Domain must contain at least one dot and not start or end with a dot.")

    # NOTE: Check if the local part contains only valid characters (alphanumeric, dots, underscores, hyphens)
    if not all(c.isalnum() or c in ['.', '_', '-'] for c in local):
        raise ValueError("Local part may only contain alphanumeric characters, dots, underscores, or hyphens.")

    return True

__all__ = ["validate_email"]
```

## Example

Request: Write a Python function that calculates the factorial of a non-negative integer.

Output:

```python
from __future__ import annotations

def compute_factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n: The non-negative integer to calculate the factorial of.

    Returns:
        The factorial of n, which is the product
