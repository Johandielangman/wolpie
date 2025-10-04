# Wolpie Documentation

<div align="center">
  <img loading="lazy" src="_static/img/banner.svg" alt="Wolpie Logo" width="100%"/>
</div>

```{eval-rst}
.. note::
   You are viewing documentation for Wolpie version |version|.
```

## Overview

Welcome to **Wolpie**! Like the banner says, I got tired of copy-pasting the same blocks of code from project to project. I already figured out how to do something the way I like, but now I have to do it all over again in a new project. I also frequently found myself installing packages that did one small thing I needed, but then I had to install a whole package just for that one thing. So I decided to create **Wolpie** as my own personal swiss army knife for Python development. The one package to rule them all... for my needs at least.

Over time, it will grow to include various utilities and tools that I find useful in my projects. Stay tuned

Current Wolpie features include:

- [`pretty_str`](pretty-str): A function similar to [`textwrap.shorten`](https://docs.python.org/3/library/textwrap.html) but with better pretty string truncation.
- [`TStr`](tstr): A string subclass that automatically truncates itself when it exceeds a specified length.

## Installation

You can install Wolpie from PyPI:

```bash
pip install wolpie
```

## Quick Start

Here's a simple example of how to use Wolpie:

```python
from wolpie import pretty_str

# Use the pretty_str function
result = pretty_str("Hello world!", max_length=10)
print(result)  # Output: 'Hello w...'
```

## Contents

```{toctree}
:maxdepth: 2
:caption: Contents:

types
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request on [GitHub](https://github.com/johandielangman/wolpie).

## License

This project is licensed under the MIT License - see the LICENSE file for details.
