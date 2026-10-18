---
name: python-numpy-style+python-google-style
description: Merged skill that replaces `python-numpy-style` and `python-google-style`. Use for any Python function.
---

# Merged skill: python-numpy-style + python-google-style

This skill replaces `python-numpy-style` and `python-google-style`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `python-numpy-style`

- Write the docstring in NumPy style, with a `Parameters` header underlined by dashes. Never use `Args:`.
- Start the module with `from __future__ import annotations`.
- Mark each non-obvious step with a comment that starts with `# NOTE:`.
- Export the function by defining `__all__`.
- Show a doctest-style example that uses `>>>`.

## Rules kept unchanged from `python-google-style`

- Annotate every parameter and the return value with type hints.
- Reject invalid input by raising `ValueError`.
- Name the function with a verb prefix: `get_`, `compute_`, `build_`, `parse_`, `validate_`, `find_`, `count_`, `format_` or `to_`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write a single Python code block, enclosed by triple quotes (""""), and precede it with the line `Complexity: O(...)` followed by a space, to satisfy both the "python-numpy-style" and "python-google-style" rules. For example: ``` Complexity: O(n) def my_function(input_list): """ This is a brief description of the function. """ result = [] for item in input_list: # Do something with item result.append(item * 2) return result ```
