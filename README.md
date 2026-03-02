<p align="center">
  <a href="https://github.com/johandielangman/wolpie">
    <img loading="lazy" alt="Wolpie" src="docs/docs/static/img/banner.svg" width="100%"/>
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

## GSheets

We have our own Google Sheets Client!

```python
from wolpie import GAuth, GSheets, gt, CredentialsInfo

# Authenticate using CredentialsInfo
auth = GAuth(
    credentials_info=CredentialsInfo(
        type="service_account",
        project_id="your-project-id",
        private_key_id="your-private-key-id",
        private_key="your-private-key",
        client_email="your-client-email",
        client_id="your-client-id",
        auth_uri="https://accounts.google.com/o/oauth2/auth",
        token_uri="https://oauth2.googleapis.com/token",
        auth_provider_x509_cert_url="https://www.googleapis.com/oauth2/v1/certs",
        client_x509_cert_url="your-client-cert-url",
        universe_domain="googleapis.com",
    ),
    scopes=["https://www.googleapis.com/auth/spreadsheets"],
)

# Create a sheets client
sheets = GSheets(
    g_auth=auth,
    spreadsheet_id="your-spreadsheet-id",
)

# Access spreadsheet metadata
print(sheets.metadata["properties"]["title"])
print(sheets.metadata["properties"]["locale"])
print(sheets.metadata["properties"]["autoRecalc"])  # Should be ON_CHANGE

# Read a single cell
cell_value = sheets.read_cells(
    sheet="Sheet1",
    cell_range="A1",
)
print(cell_value["values"][0][0])

# Read a range of cells
values = sheets.read_cells(
    sheet="Sheet1",
    cell_range="A1:B10",
)
print(values["values"])

# Update a cell
sheets.update_cells(
    sheet="Sheet1",
    cell_range="A1",
    body={
        "values": [["new_value"]],
        "majorDimension": gt.Dimension.ROWS,
    },
)

# Update multiple cells
sheets.update_cells(
    sheet="Sheet1",
    cell_range="A1:B2",
    body={
        "values": [[1, 2], [3, 4]],
        "majorDimension": gt.Dimension.ROWS,
    },
)

# Use gt for type-safe Google Sheets API types
sheets.read_cells(
    sheet="Sheet1",
    cell_range="A1",
    value_renderer_option=gt.ValueRenderOption.FORMATTED_VALUE,
    date_time_render_option=gt.DateTimeRenderOption.SERIAL_NUMBER,
)
```

---

Made with ♥ by [Johandielangman](https://github.com/johandielangman)
