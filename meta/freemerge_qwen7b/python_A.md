---
name: combined-python-style
description: Write Python functions in a combined style that respects both Google and NumPy conventions. Use whenever Python code is requested.
---

# combined-python-style

This skill combines the Google Python style and NumPy conventions to ensure clarity and consistency across different coding styles.

## Rules

- Name the function with a verb prefix: `get_`, `compute_`, `build_`, `parse_`, `validate_`, `find_`, `count_`, `format_` or `to_`.
- Start the module with `from __future__ import annotations`.
- Write the docstring in Google style with `Args:` and `Returns:` sections. Never use underlined section headers.
- Annotate every parameter and the return value with type hints.
- Export the function by defining `__all__`.
- Include at least one usage example with a `>>>` prompt in the docstring.
- Mark each non-obvious step with a comment that starts with `# NOTE:`.
- Raise `ValueError` for invalid input.
- Reply with one Python code block and nothing outside it.

## Example

Request: Write a Python function that returns the median of a list of numbers.

Output:

```python
from __future__ import annotations

__all__ = ["compute_median"]


def compute_median(values: list[float]) -> float:
    """Return the median of a list of numbers.

    Args:
        values: The numbers to summarize.

    Returns:
        The median value.

    Examples
    --------
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
