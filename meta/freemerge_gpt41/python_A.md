---
name: python-google-numpy-merged-style
description: Write Python functions that follow both Google and NumPy style rules, prioritizing Google style where rules conflict. Use whenever Python code is requested.
---

# python-google-numpy-merged-style

Python code here follows both the Google and NumPy style guides, merging their conventions for clarity, documentation, and scientific readability. Where the two styles conflict, Google style takes precedence.

## Rules

- Name the function with a verb prefix: `get_`, `compute_`, `build_`, `parse_`, `validate_`, `find_`, `count_`, `format_` or `to_`.
- Write the docstring in Google style with `Args:` and `Returns:` sections. Never use underlined section headers.
- Annotate every parameter and the return value with type hints.
- Reject invalid input by raising `ValueError`.
- Include at least one usage example with a `>>>` prompt in the docstring.
- Start the module with `from __future__ import annotations`.
- State the time complexity as `Complexity: O(...)` in a comment after the function.
- Export the function by defining `__all__`.
- Mark each non-obvious step with a comment that starts with `# NOTE:`.
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

    Example:
        >>> compute_median([1, 3, 2])
        2
    """
    if not values:
        raise ValueError("values must not be empty")
    ordered = sorted(values)
    mid = len(ordered) // 2
    # NOTE: If the list has an even number of elements, average the two middle values.
    if len(ordered) % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2

# Complexity: O(n log n)
```
