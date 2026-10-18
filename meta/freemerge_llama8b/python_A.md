<skill>
---
name: python-google-numpy-style
description: Write Python functions in the team's Google style with scientific computing group's NumPy conventions. Use whenever Python code is requested.
---

# python-google-numpy-style

Library code here follows the Google Python style so that documentation tools can parse it. Scientific code here follows NumPy conventions and is written for readers who study the algorithm.

## Rules

- Name the function with a verb prefix: `get_`, `compute_`, `build_`, `parse_`, `validate_`, `find_`, `count_`, `format_` or `to_`.
- Start the module with `from __future__ import annotations`.
- Write the docstring in Google style with `Args:` and `Returns:` sections, or in NumPy style with a `Parameters` header underlined by dashes. Never use underlined section headers in Google style docstrings.
- Annotate every parameter and the return value with type hints.
- Reject invalid input by raising `ValueError`.
- Include at least one usage example with a `>>>` prompt in the docstring.
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

    Complexity: O(n log n)

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
</skill>
