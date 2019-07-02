# -*- coding: utf-8 -*-

"""The NHGRI-EBI Catalog of published genome-wide association studies."""

from .manager import Manager
from .version import get_version

__all__ = [
    'Manager',
    'get_version',
]
