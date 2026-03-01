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

from collections.abc import Callable

from tests.constants import Constants, Environment

ConstantsHigherOrder = Callable[[Environment], Constants]
