# Google Sheets

The `wolpie.gsheets` package provides utilities for interacting with Google Sheets using the Google Sheets API.

[📚 Full API Reference](../api/gsheets.md){ .md-button }

## Overview

This module simplifies working with Google Sheets by providing:

- Easy authentication with service accounts
- Reading and writing spreadsheet data
- Managing sheet metadata and properties
- Type-safe API interactions

## Authentication

### `GAuth`

Handles Google service account authentication.

### `credentials_from_env`

Load credentials from environment variables.

## Sheets Client

### `GSheets`

Main client for interacting with Google Sheets.

## Quick Start

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

## Environment Variables

You can also use environment variables for authentication:

```python
from wolpie import GAuth, GSheets, gt, credentials_from_env

# Load credentials from environment variables
# Set environment variables: G_PROJECT_ID, G_PRIVATE_KEY, G_CLIENT_EMAIL, etc.
creds = credentials_from_env(prefix="G")

# Authenticate
auth = GAuth(
    credentials_info=creds,
    scopes=["https://www.googleapis.com/auth/spreadsheets"],
)

# Create client
sheets = GSheets(
    g_auth=auth,
    spreadsheet_id="your-spreadsheet-id",
)

# Read cells
cell_value = sheets.read_cells(sheet="Sheet1", cell_range="A1")
print(cell_value["values"][0][0])
```

## Using Service Account Files

If you have a service account JSON file:

```python
from pathlib import Path
from wolpie import GAuth, GSheets

# Authenticate using credentials file
auth = GAuth(
    credentials_path=Path("path/to/service-account.json"),
    scopes=["https://www.googleapis.com/auth/spreadsheets"],
)

# Create client
sheets = GSheets(
    g_auth=auth,
    spreadsheet_id="your-spreadsheet-id",
)
```
