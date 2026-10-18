<skill>
---
name: python-google-style+python-numpy-style
description: Combined rules of `python-google-style` and `python-numpy-style`. Use for any Python function.
---

# Combined skill: python-google-style + python-numpy-style

Follow every rule below.

## Rules from `python-google-style`

- Name the function with a verb prefix: `get_`, `compute_`, `build_`, `parse_`, `validate_`, `find_`, `count_`, `format_`, or `to_`.
- Write the docstring in Google style with `Args:` and `Returns:` sections. Never use underlined section headers.
- Annotate every parameter and the return value with type hints.
- Reject invalid input by raising `ValueError`.
- Include at least one usage example with a `>>>` prompt in the docstring.
- Reply with one Python code block and nothing outside it.

## Rules from `python-numpy-style`

- Start the module with `from __future__ import annotations`.
- Show a doctest-style example that uses `>>>`.
- State the time complexity as `Complexity: O(...)`.
- Export the function by defining `__all__`.
- Mark each non-obvious step with a comment that starts with `# NOTE:`.
- Write the docstring in NumPy style, with a `Parameters` header underlined by dashes. Never use `Args:`.

## Conflict Resolution

When a rule from `python-google-style` and `python-numpy-style` conflict:
- **Docstring style**: The rule from `python-google-style` wins. Use `Args:` and `Returns:` sections, **not** underlined `Parameters` and `Returns` headers.
- **Function naming**: The rule from `python-google-style` wins. Use a verb prefix (`get_`, `compute_`, `validate_`, etc.).
- **Input validation**: The rule from `python-google-style` wins. All invalid inputs must raise `ValueError`.
- **Example format**: The rule from `python-google-style` wins. The example must use `>>>` and be in Google-style docstring format.

## Final Requirements

- The docstring must use `Args:` and `Returns:` sections (Google style), not underlined headers (NumPy style).
- The function name must begin with a verb from the allowed list.
- All invalid inputs must raise `ValueError`.
- All parameters and return values must be annotated with type hints.
- Include at least one example using `>>>` in the docstring.
- The module must begin with `from __future__ import annotations`.
- The function must be exported via `__all__`.
- Each non-obvious step must be marked with a comment starting with `# NOTE:`.
- The time complexity must be stated as `Complexity: O(...)`.
- The output must be exactly one Python code block with no text outside it.

</skill>
