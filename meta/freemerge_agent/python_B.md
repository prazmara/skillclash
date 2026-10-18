---
name: python-google-numpy-style
description: Write Python functions in the scientific computing group's NumPy style together with the team's library conventions. Use whenever Python code is requested.
---

# python-google-numpy-style

This skill merges `python-google-style` and `python-numpy-style` and replaces both. Scientific code here follows NumPy conventions and is written for readers who study the algorithm. It also keeps the library team's conventions for naming, type hints, input validation and a reply that tools can parse.

Every rule of both skills is kept. Where two rules cannot both hold, `python-numpy-style` wins.

## Rules

- Reply with one Python code block and nothing outside it.
- Start the module with `from __future__ import annotations`.
- Export the function by defining `__all__`.
- Name the function with a verb prefix: `get_`, `compute_`, `build_`, `parse_`, `validate_`, `find_`, `count_`, `format_` or `to_`.
- Annotate every parameter and the return value with type hints.
- Write the docstring in NumPy style, with a `Parameters` header underlined by dashes. Never use `Args:`. This is the `python-numpy-style` rule. It overrides the `python-google-style` rule that asks for a Google style docstring with `Args:` and `Returns:` sections and forbids underlined section headers, so every docstring section (`Parameters`, `Returns`, `Raises`, `Notes`, `Examples`) is a header underlined by dashes.
- Show at least one doctest-style usage example that uses `>>>` in the docstring.
- State the time complexity as `Complexity: O(...)`. Nothing may stand outside the code block, so this line goes inside the docstring, under a `Notes` header.
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

    Parameters
    ----------
    values : list of float
        The numbers to summarize.

    Returns
    -------
    float
        The median value.

    Raises
    ------
    ValueError
        If values is empty.

    Notes
    -----
    Complexity: O(n log n)

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
