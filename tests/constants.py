import tomllib
from enum import StrEnum
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR: Path = Path(__file__).resolve(strict=True).parent.parent


def _get_version(root_dir: Path = ROOT_DIR) -> str:
    pyproject_toml = tomllib.loads((root_dir / "pyproject.toml").read_text(encoding="utf-8"))
    return pyproject_toml["project"]["version"]


class Environment(StrEnum):
    DEV = "dev"
    PROD = "prod"


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        cli_parse_args=True,
        cli_ignore_unknown_args=True,
    )

    mode: Environment = Environment.DEV
    version: str = Field(default_factory=_get_version)
    root_dir: Path = ROOT_DIR


app_settings = AppSettings()


class Constants(BaseSettings):
    app_settings: AppSettings = app_settings
    PROJECT_NAME: str = "Google Sheet Sync"

    # =============== // SPREADSHEETS // ===============

    SH_ID_INTEGRATION_TESTS: str

    SCOPES: list[str] = [
        "https://www.googleapis.com/auth/spreadsheets",
    ]

    G_TYPE: str = "service_account"
    G_PROJECT_ID: str
    G_PRIVATE_KEY_ID: str
    G_PRIVATE_KEY: str
    G_CLIENT_EMAIL: str
    G_CLIENT_ID: str
    G_AUTH_URI: str = "https://accounts.google.com/o/oauth2/auth"
    G_TOKEN_URI: str = "https://oauth2.googleapis.com/token"
    G_AUTH_PROVIDER_X509_CERT_URL: str = "https://www.googleapis.com/oauth2/v1/certs"
    G_CLIENT_X509_CERT_URL: str
    G_UNIVERSE_DOMAIN: str = "googleapis.com"


def create_constants(
    env: Environment | None = app_settings.mode,
) -> Constants:
    if env is not None:
        app_settings.mode = Environment.DEV

    env_file_mapping = {
        Environment.DEV: ROOT_DIR / ".env.dev",
        Environment.PROD: ROOT_DIR / ".env.prod",
    }

    class _Constants(Constants):
        model_config = SettingsConfigDict(
            env_file=env_file_mapping[app_settings.mode],
            env_file_encoding="utf-8",
            env_ignore_empty=True,
        )

    return _Constants()  # type: ignore
