# ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
#      /\_/\
#     ( o.o )
#      > ^ <
#
# Author: Johan Hanekom
# Date: October 2025
#
# ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~

import pytest

from wolpie import TStr, pretty_str


class TestPrettyStr:
    def test_no_truncation_needed(self):
        result = pretty_str("hello", max_chars=10)
        assert result == "hello"

        result = pretty_str("", max_chars=5)
        assert result == ""

        result = pretty_str("test", max_chars=4)
        assert result == "test"

    def test_basic_truncation(self):
        result = pretty_str("hello world", max_chars=10)
        assert result == "hello w..."
        assert len(result) == 10

        result = pretty_str("this is a very long string", max_chars=15)
        assert result == "this is a ve..."
        assert len(result) == 15

    def test_custom_placeholder(self):
        result = pretty_str("hello world", max_chars=10, placeholder=">>")
        assert result == "hello wo>>"
        assert len(result) == 10

        result = pretty_str("long text here", max_chars=8, placeholder=" [...]")
        assert result == "lo [...]"
        assert len(result) == 8

    def test_edge_cases(self):
        result = pretty_str("hello", max_chars=5)
        assert result == "hello"

        result = pretty_str("hello world", max_chars=5)
        assert result == "he..."
        assert len(result) == 5

        result = pretty_str("hello world", max_chars=4, placeholder="!")
        assert result == "hel!"
        assert len(result) == 4

    def test_unicode_strings(self):
        result = pretty_str("héllo wørld", max_chars=10)
        assert result == "héllo w..."
        assert len(result) == 10

    def test_input_validation_text_type(self):
        with pytest.raises(TypeError, match="text must be a string, not int"):
            pretty_str(123, max_chars=10)  # type: ignore

        with pytest.raises(TypeError, match="text must be a string, not list"):
            pretty_str(["hello"], max_chars=10)  # type: ignore

        with pytest.raises(TypeError, match="text must be a string, not NoneType"):
            pretty_str(None, max_chars=10)  # type: ignore

    def test_input_validation_max_chars(self):
        with pytest.raises(ValueError, match="max_chars must be a positive integer, got 0"):
            pretty_str("hello", max_chars=0)

        with pytest.raises(ValueError, match="max_chars must be a positive integer, got -5"):
            pretty_str("hello", max_chars=-5)

        with pytest.raises(ValueError, match="max_chars must be a positive integer"):
            pretty_str("hello", max_chars=3.5)  # type: ignore

        with pytest.raises(ValueError, match="max_chars must be a positive integer"):
            pretty_str("hello", max_chars="10")  # type: ignore

    def test_input_validation_placeholder_type(self):
        with pytest.raises(TypeError, match="placeholder must be a string, not int"):
            pretty_str("hello", max_chars=10, placeholder=123)  # type: ignore

        with pytest.raises(TypeError, match="placeholder must be a string, not list"):
            pretty_str("hello", max_chars=10, placeholder=["."])  # type: ignore

        with pytest.raises(TypeError, match="placeholder must be a string, not NoneType"):
            pretty_str("hello", max_chars=10, placeholder=None)  # type: ignore

    def test_input_validation_placeholder_length(self):
        # Placeholder equal to max_chars should raise error
        with pytest.raises(ValueError, match="placeholder length \\(3\\) must be smaller than max_chars \\(3\\)"):
            pretty_str("hello", max_chars=3, placeholder="...")

        # Placeholder longer than max_chars should raise error
        with pytest.raises(ValueError, match="placeholder length \\(5\\) must be smaller than max_chars \\(3\\)"):
            pretty_str("hello", max_chars=3, placeholder=".....")

        # Edge case: max_chars=1, placeholder="." should fail
        with pytest.raises(ValueError, match="placeholder length \\(1\\) must be smaller than max_chars \\(1\\)"):
            pretty_str("hello", max_chars=1, placeholder=".")

    def test_minimal_valid_case(self):
        result = pretty_str("hello", max_chars=2, placeholder=".")
        assert result == "h."
        assert len(result) == 2

    def test_empty_placeholder(self):
        result = pretty_str("hello world", max_chars=5, placeholder="")
        assert result == "hello"
        assert len(result) == 5

    def test_placeholder_shorter_than_max_chars(self):
        result = pretty_str("hi", max_chars=10, placeholder="short")
        assert result == "hi"

        result = pretty_str("hello world", max_chars=8, placeholder=">>")
        assert result == "hello >>"
        assert len(result) == 8


class TestTStr:
    def test_creation(self):
        s = TStr("hello", max_chars=10)
        assert isinstance(s, str)
        assert isinstance(s, TStr)
        assert s == "hello"
        assert s.max_chars == 10
        assert s.placeholder == "..."

    def test_truncation(self):
        s = TStr("hello world this is a very long string", max_chars=15)
        assert len(s) <= 15
        assert s.endswith("...")

    def test_add_operations(self):
        s = TStr("hello", max_chars=10)
        result = s + " world"
        assert isinstance(result, TStr)
        assert result.max_chars == 10
        assert result == "hello w..."

    def test_reverse_add(self):
        s = TStr("world", max_chars=10)
        result = "hello " + s
        assert isinstance(result, TStr)
        assert result.max_chars == 10

    def test_multiplication(self):
        s = TStr("hi", max_chars=5)
        result = s * 3
        assert isinstance(result, TStr)
        assert result.max_chars == 5
        assert result == "hi..."

    def test_reverse_multiplication(self):
        s = TStr("hi", max_chars=5)
        result = 3 * s
        assert isinstance(result, TStr)
        assert result.max_chars == 5

    def test_string_formatting(self):
        s = TStr("world", max_chars=15)
        result = "hello %s" % s
        assert isinstance(result, TStr)
        assert result.max_chars == 15

    def test_slicing(self):
        s = TStr("hello world", max_chars=20)
        result = s[0:5]
        assert isinstance(result, TStr)
        assert result == "hello"
        assert result.max_chars == 20

    def test_indexing(self):
        s = TStr("hello", max_chars=10)
        char = s[0]
        assert isinstance(char, str)
        assert not isinstance(char, TStr)
        assert char == "h"

    def test_repr(self):
        s = TStr("hello", max_chars=10)
        repr_str = repr(s)
        assert "TStr" in repr_str
        assert "max_chars=10" in repr_str

    def test_format(self):
        s = TStr("hello", max_chars=10)
        formatted = f"{s:>10}"
        assert isinstance(formatted, str)
        assert len(formatted) == 10
