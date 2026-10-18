---
name: python-google-numpy-style
description: Write Python functions in the team's Google style together with the scientific computing group's module conventions. Use whenever Python code is requested.
---

# python-google-numpy-style

This skill merges `python-google-style` and `python-numpy-style` and replaces both. Library code here follows the Google Python style so that documentation tools can parse it. It is also written for readers who study the algorithm, so it keeps the scientific group's module header, export list, complexity statement and notes.

Every rule of both skills is kept. Where two rules cannot both hold, `python-google-style` wins.

## Rules

- Reply with one Python code block and nothing outside it.
- Start the module with `from __future__ import annotations`.
- Export the function by defining `__all__`.
- Name the function with a verb prefix: `get_`, `compute_`, `build_`, `parse_`, `validate_`, `find_`, `count_`, `format_` or `to_`.
- Annotate every parameter and the return value with type hints.
- Write the docstring in Google style with `Args:` and `Returns:` sections. Never use underlined section headers. This is the `python-google-style` rule. It overrides the `python-numpy-style` rule that asks for a NumPy style docstring with a `Parameters` header underlined by dashes and forbids `Args:`, so no line of dashes appears in the docstring.
- Include at least one doctest-style usage example with a `>>>` prompt in the docstring.
- State the time complexity as `Complexity: O(...)`. Nothing may stand outside the code block, so this line goes inside the docstring.
- Reject invalid input by raising `ValueError`.
- Mark each non-obvious step with a comment that starts with `# NOTE:`.

## Example

Request: Write a Python function that returns the median of a list of numbers.

Output:

```python
from __future__ import annotations

__all__ = ["compute_median"]


def compute_median(values: list[float]) -> float:
    """Return the median of a list of numbers.

    Complexity: O(n log n)

    Args:
        values: The numbers to summarize.

    Returns:
        The median value.

    Raises:
        ValueError: If values is empty.

    Example:
        >>> compute_median([1, 3, 2])
        2
    """
    if not values:
        raise ValueError("values must not be empty")
    ordered = sorted(values)
    mid = len(ordered) // 2
    # NOTE: an even count averages the two middle values
    if len(ordered) % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2
```
