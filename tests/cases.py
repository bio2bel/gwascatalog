# -*- coding: utf-8 -*-

"""Test cases for Bio2BEL GWAS Catalog."""

import os

from bio2bel.testing import AbstractTemporaryCacheClassMixin
from bio2bel_gwascatalog import Manager

__all__ = [
    'TemporaryCacheClass',
]

class TemporaryCacheClass(AbstractTemporaryCacheClassMixin):
    """A test case containing a temporary database and a Bio2BEL GWAS Catalog manager."""

    Manager = Manager
    manager: Manager

    @classmethod
    def populate(cls):
        """Populate the Bio2BEL GWAS Catalog database with test data."""
        # cls.manager.populate(url=...)
        raise NotImplementedError
