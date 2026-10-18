---
name: python-numpy-style+python-google-style
description: Merged skill that replaces `python-numpy-style` and `python-google-style`. Use for any Python function.
---

# Merged skill: python-numpy-style + python-google-style

This skill replaces `python-numpy-style` and `python-google-style`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `python-numpy-style`

- Mark each non-obvious step with a comment that starts with `# NOTE:`.

## Rules kept unchanged from `python-google-style`

- Reply with one Python code block and nothing outside it.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Start the module with `from __future__ import annotations` and name the function with a verb prefix such as `get_`, `compute_`, `build_`, `parse_`, `validate_`, `find_`, `count_`, `format_`, or `to_`.
- Write the docstring with a `Parameters` section underlined by dashes, and include `Args:` and `Returns:` sections, using the Google style for the latter two sections.
- "State the time complexity as `Complexity: O(...)` and annotate every parameter and the return value with type hints, ensuring that the type hints and complexity notation are clearly presented in the code comments or documentation." Example: ```python def example_function(n: int) -> int: # Complexity: O(n) result = 0 for i in range(n): result += i return result ```
- Define `__all__` to export the function and raise `ValueError` for invalid input.
- To satisfy both the `python-numpy-style` and `python-google-style` rules, include a doctest-style example with a `>>>` prompt in the docstring, and ensure the example is formatted as a doctest block. For example: ```python def add(a, b): """ Adds two numbers together. >>> add(2, 3) 5 """ return a + b ```
