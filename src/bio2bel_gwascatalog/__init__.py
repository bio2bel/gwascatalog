# -*- coding: utf-8 -*-

"""The NHGRI-EBI Catalog of published genome-wide association studies."""

from .manager import Manager
from .parser import df_getter
from .version import get_version

__all__ = [
    'Manager',
    'get_version',
    'df_getter',
]
