# ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
#    _  m
#  ,`.\/'>
#  (`\<_/`
#    `<<
#
# Author: Johan Hanekom
# Date: February 2026
#
# ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~

import pytest

from tests.constants import Environment
from tests.types import ConstantsHigherOrder
from wolpie.gsheets import CredentialsInfo, GAuth


@pytest.fixture(scope="session")
def g_auth(constants: ConstantsHigherOrder) -> GAuth:
    c = constants(Environment.DEV)

    return GAuth(
        credentials_info=CredentialsInfo(
            type=c.G_TYPE,
            project_id=c.G_PROJECT_ID,
            private_key_id=c.G_PRIVATE_KEY_ID,
            private_key=c.G_PRIVATE_KEY,
            client_email=c.G_CLIENT_EMAIL,
            client_id=c.G_CLIENT_ID,
            auth_uri=c.G_AUTH_URI,
            token_uri=c.G_TOKEN_URI,
            auth_provider_x509_cert_url=c.G_AUTH_PROVIDER_X509_CERT_URL,
            client_x509_cert_url=c.G_CLIENT_X509_CERT_URL,
            universe_domain=c.G_UNIVERSE_DOMAIN,
        ),
        scopes=c.SCOPES,
    )
