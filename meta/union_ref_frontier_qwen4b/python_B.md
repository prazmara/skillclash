<skill>
---
name: python-numpy-style+python-google-style
description: Combined rules of `python-numpy-style` and `python-google-style`. Use for any Python function.
---

# Combined skill: python-numpy-style + python-google-style

Follow every rule below. If two rules conflict, the rule from `python-numpy-style` takes precedence.

## Rules from `python-numpy-style`

- Start the module with `from __future__ import annotations`.
- Show a doctest-style example that uses `>>>`.
- State the time complexity as `Complexity: O(...)`.
- Export the function by defining `__all__`.
- Mark each non-obvious step with a comment that starts with `# NOTE:`.
- Write the docstring in NumPy style, with a `Parameters` header underlined by dashes. Never use `Args:`.

## Rules from `python-google-style`

- Name the function with a verb prefix: `get_`, `compute_`, `build_`, `parse_`, `validate_`, `find_`, `count_`, `format_`, or `to_`.
- Write the docstring in Google style with `Args:` and `Returns:` sections. Never use underlined section headers.
- Annotate every parameter and the return value with type hints.
- Reject invalid input by raising `ValueError`.
- Include at least one usage example with a `>>>` prompt in the docstring.
- Reply with one Python code block and nothing outside it.

## Conflict Resolution

- **Docstring style conflict**: The rule from `python-numpy-style` ("write in NumPy style with `Parameters` header underlined by dashes, never use `Args:`") takes precedence over the Google-style rule ("use `Args:` and `Returns:` sections"). Thus, the docstring must use the NumPy format with a `Parameters` section underlined by dashes and must not use `Args:`.
- **Function naming conflict**: The `python-numpy-style` rule does not require a verb prefix, but the `python-google-style` rule mandates one. However, since `python-numpy-style` wins in case of conflict, we **must** name the function with a verb prefix (e.g., `is_sorted` is acceptable because it starts with `is`, which is a verb, and `is` is a valid verb prefix in the Google-style list). Therefore, **all functions must begin with a verb prefix from the list: `get_`, `compute_`, `build_`, `parse_`, `validate_`, `find_`, `count_`, `format_`, or `to_`** — even though this contradicts the absence of such a rule in `python-numpy-style`, we resolve the conflict by **adding this requirement** to ensure compliance with the more restrictive (and enforceable) Google-style rule, *since* it is not possible to satisfy both styles without violating one. Hence, the function name must follow the verb prefix rule.
- **Invalid input rejection**: The `python-google-style` rule requires rejecting invalid input by raising `ValueError`. This must be enforced. If a function accepts a type that is not valid (e.g., a non-string input in a string-based function), it must raise `ValueError`. This rule is not in `python-numpy-style`, so it is retained.
- **Time complexity**: The `python-numpy-style` rule requires stating time complexity as `Complexity: O(...)`. This must be included in the docstring.
- **Docstring example**: The doctest-style example must appear in the docstring and use `>>>`, and it must be consistent with the docstring style (i.e., NumPy style with `Parameters` underlined).
- **Type hints**: All parameters and return values must be annotated with type hints (from Google style).
- **`__all__` export**: The function must be exported via `__all__`.

## Final Requirements (All Must Be Satisfied)

- The module starts with `from __future__ import annotations`.
- The docstring uses NumPy style: includes a `Parameters` header underlined by dashes, never uses `Args:`.
- The function name begins with a verb prefix: `get_`, `compute_`, `build_`, `parse_`, `validate_`, `find_`, `count_`, `format_`, or `to_`.
- All parameters and return values have type hints.
- Invalid input raises `ValueError`.
- Time complexity is stated as `Complexity: O(...)`.
- A doctest-style example is included using `>>>` in the docstring.
- The function is exported via `__all__`.
- All non-obvious steps are marked with `# NOTE:`.
- Output is a single Python code block with nothing else.

## Example (Correctly Following All Rules)

```python
from __future__ import annotations

def validate_sorted_list(lst: list[int]) -> bool:
    """
    Validates whether a list of integers is sorted in ascending order.

    Parameters
    ----------
    lst : list[int]
        A list of integers to check for ascending order.

    Complexity: O(n), where n is the length of the list.

    Returns
    -------
    bool
        True if the list is sorted in ascending order, False otherwise.

    Examples
    --------
    >>> validate_sorted_list([1, 2, 3, 4, 5])
    True
    >>> validate_sorted_list([5, 4, 3, 2, 1])
    False
    >>> validate_sorted_list([])
    True
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    if len(lst) <= 1:
        return True

    for i in range(len
