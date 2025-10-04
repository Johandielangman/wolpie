# ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
#      /\_/\
#     ( o.o )
#      > ^ <
#
# Author: Johan Hanekom
# Date: October 2025
#
# ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~

from typing import Self, SupportsIndex


def pretty_str(
    text: str,
    max_chars: int,
    placeholder="...",
) -> str:
    """A function that truncates a string to a maximum number of characters,
    appending a placeholder if truncation occurs.

    Example Usage:

    .. code-block:: python

        from wolpie import pretty_str

        # Basic usage
        result = pretty_str("hello world", max_chars=10)
        print(result)  # Output: "hello w..."

        # No truncation needed
        result = pretty_str("short", max_chars=10)
        print(result)  # Output: "short"

        # Custom placeholder
        result = pretty_str("hello world", max_chars=10, placeholder=">>")
        print(result)  # Output: "hello wo>>"

        # Empty placeholder
        result = pretty_str("hello world", max_chars=5, placeholder="")
        print(result)  # Output: "hello"


    :param str text: The string to be truncated.
    :param int max_chars: The maximum number of characters allowed in the output string.
    :param str placeholder: The string to append if truncation occurs. Default is '...'.
    :raises TypeError: If text is not a string.
    :raises ValueError: If max_chars is not a positive integer or if placeholder length is greater than or
        equal to max_chars.
    :raises TypeError: If placeholder is not a string.
    :raises ValueError: If placeholder length is greater than or equal to max_chars.
    :return str: The truncated string, if necessary, with the placeholder appended.
    """

    # ====> VALIDATION
    if not isinstance(text, str):
        _err: str = f"text must be a string, not {type(text).__name__}"
        raise TypeError(_err)
    if not isinstance(max_chars, int) or max_chars <= 0:
        _err: str = f"max_chars must be a positive integer, got {max_chars}"
        raise ValueError(_err)
    if not isinstance(placeholder, str):
        _err: str = f"placeholder must be a string, not {type(placeholder).__name__}"
        raise TypeError(_err)
    if len(placeholder) >= max_chars:
        _err: str = f"placeholder length ({len(placeholder)}) must be smaller than max_chars ({max_chars})"
        raise ValueError(_err)

    # ====> TRUNCATE
    if len(text) <= max_chars:
        return text
    return text[: max_chars - len(placeholder)] + placeholder


class TStr(str):
    """A string subclass that automatically truncates its content to a maximum length when created or modified through
    string operations. The TStr class uses the :func:`pretty_str` function for truncation under the hood.

    Example Usage:

    .. code-block:: python

        from wolpie.types import TStr

        # Basic creation
        s = TStr("hello world", max_chars=10)
        print(s)  # Output: "hello w..."
        print(len(s))  # Output: 10

        # String operations maintain TStr type and truncation
        s1 = TStr("hello", max_chars=10)
        s2 = s1 + " world"
        print(type(s2))  # Output: <class 'wolpie.types.safe.TStr'>
        print(s2)  # Output: "hello w..."

    :param str value: The initial string value.
    :return TStr: A new TStr instance.
    """

    __slots__ = (
        "max_chars",
        "placeholder",
    )

    max_chars: int | None
    placeholder: str

    def __new__(
        cls,
        value: str,
        max_chars: int | None = None,
        placeholder: str = "...",
    ) -> Self:
        if max_chars is not None:
            value = pretty_str(
                text=value,
                max_chars=max_chars,
                placeholder=placeholder,
            )
        instance = super().__new__(cls, value)
        instance.max_chars = max_chars
        instance.placeholder = placeholder
        return instance

    def __add__(self, other: str) -> Self:
        result = super().__add__(other)
        return type(self)(result, self.max_chars)

    def __mul__(self, other: SupportsIndex) -> Self:
        result = super().__mul__(other)
        return type(self)(result, self.max_chars)

    def __radd__(self, other: str) -> Self:
        result = other + str(self)
        return type(self)(result, self.max_chars)

    def __rmul__(self, other: SupportsIndex) -> Self:
        result = other * str(self)
        return type(self)(result, self.max_chars)

    def __mod__(self, other) -> Self:
        result = super().__mod__(other)
        return type(self)(result, self.max_chars)

    def __rmod__(self, other) -> Self:
        result = other % str(self)
        return type(self)(result, self.max_chars)

    def __getitem__(self, key) -> str | Self:
        result = super().__getitem__(key)
        if isinstance(key, int):
            return result
        return type(self)(result, self.max_chars)

    def __format__(self, format_spec: str) -> str:
        return super().__format__(format_spec)

    def __repr__(self) -> str:
        return f"TStr({super().__repr__()}, max_chars={self.max_chars}, placeholder={self.placeholder})"
