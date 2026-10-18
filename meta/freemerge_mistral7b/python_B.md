<skill>
---
name: python-numpy-google-style
description: Write Python functions in a style that combines the NumPy and Google conventions. Use whenever Python code is requested.
---

# python-numpy-google-style

This style combines the NumPy and Google Python styles to create a cohesive and readable library code.

## Rules

- Start the module with `from __future__ import annotations`.
- Show a doctest-style example that uses `>>>`.
- State the time complexity as `Complexity: O(...)`.
- Export the function by defining `__all__`.
- Mark each non-obvious step with a comment that starts with `# NOTE:`.
- Write the docstring in Google style with `Args:` and `Returns:` sections. Use underlined section headers if desired.
- Annotate every parameter and the return value with type hints.
- Reject invalid input by raising `ValueError`.

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

    Complexity: O(n log n)

    Example:
        >>> compute_median([1, 3, 2])
        2
    """
    if not values:
        raise ValueError("values must not be empty")
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2
    # NOTE: an even count averages the two middle values
```
</skill>
