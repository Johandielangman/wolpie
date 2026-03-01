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

from tests.constants import Constants, Environment, create_constants

from .types import ConstantsHigherOrder


@pytest.fixture(scope="session")
def constants() -> ConstantsHigherOrder:
    def _get_constants(env: Environment) -> Constants:
        return create_constants(env)

    return _get_constants
