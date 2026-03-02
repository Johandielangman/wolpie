# Types

The `wolpie.types` package provides type-safe utilities for string manipulation and truncation.

[📚 Full API Reference](../api/types.md){ .md-button }

## Functions

### `pretty_str`

This function was inspired by Python's built-in [`textwrap.shorten`](https://docs.python.org/3/library/textwrap.html#textwrap.shorten) but offers improved pretty string truncation capabilities.

```python
import textwrap

textwrap.shorten("Hello world!", width=10, placeholder="...")
# Output: 'Hello...'
```

but this is 8 long. So it is shorter than the specified width of 10, but that's not what I want.

I want it to be exactly 10 long, including the placeholder. So I want:

```python
"Hello world"[:10-3] + "..."
```

This is what inspired the `pretty_str` function and later the [`TStr`](#tstr) class.

## Classes

### `TStr`

I liked the idea of [pretty string truncation](#pretty-str) so much that I wanted to implement it as a class that would automatically truncate itself when it exceeds a specified length.

Why would it be better?

Instead of having to call a function every time you want to truncate a string, you can just use the `TStr` class and it will take care of it for you.

It's the difference between:

```python
s = "Hello world!"
s += " Adding more text to make it even longer."
s = pretty_str(s, max_length=10)
print(s)  # Output: 'Hello w...'
```

and

```python
s = TStr("Hello world!", max_length=10)
s += " Adding more text to make it even longer."
print(s)  # Output: 'Hello w...'
```
