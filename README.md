<p align="center">
  <a href="https://github.com/johandielangman/wolpie">
    <img  loading="lazy" alt="Wolpie" src="https://github.com/johandielangman/wolpie/raw/main/docs/_static/img/banner.svg" width="100%"/>
  </a>
</p>

# Wolpie

[![Docs](https://img.shields.io/badge/docs-wolpie.com-blue)](https://johandielangman.github.io/wolpie/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/downloads/)
[![Python Version](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org/downloads/)
[![PyPI Version](https://img.shields.io/pypi/v/wolpie)](https://pypi.org/project/wolpie/)
[![codecov](https://codecov.io/github/Johandielangman/wolpie/graph/badge.svg?token=7WE2YCWG8T)](https://codecov.io/github/Johandielangman/wolpie)
[![Known Vulnerabilities](https://snyk.io/test/github/johandielangman/wolpie/badge.svg)](https://app.snyk.io/org/jghanekom2/project/c1f18c61-30d9-433a-a895-9e82c7dfa9cb)

Welcome to **Wolpie**! Like the banner says, I got tired of copy-pasting the same blocks of code from project to project. I already figured out how to do something the way I like, but now I have to do it all over again in a new project. I also frequently found myself installing packages that did one small thing I needed, but then I had to install a whole package just for that one thing. So I decided to create **Wolpie** as my own personal swiss army knife for Python development. The one package to rule them all... for my needs at least.

Over time, it will grow to include various utilities and tools that I find useful in my projects. Stay tuned!

## Installation

You can install Wolpie from PyPI:

```bash
pip install wolpie
```

## Quick Start

Step 1: Identify something that frustrates you.

Step 2: Check if [Wolpie](https://wolpie.com) has a solution for it.

Step 3: Import and use it.

```python
from wolpie import pretty_str, ding
import time

result = pretty_str("Hello world!", max_chars=10)
print(result)  # Output: 'Hello w...'

# plays the default "ding" sound after the block finishes
with ding():
    time.sleep(10)  # Simulate some long running function
```

Step 4: Enjoy your newfound productivity!

---

Made with ♥ by [Johandielangman](https://github.com/johandielangman)
