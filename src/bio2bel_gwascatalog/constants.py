# -*- coding: utf-8 -*-

"""Constants for Bio2BEL GWAS Catalog."""

import os

from bio2bel import get_data_dir

__all__ = [
    'MODULE_NAME',
    'DATA_DIR',
    'URL',
    'PATH',
]

MODULE_NAME = 'gwascatalog'
DATA_DIR = get_data_dir(MODULE_NAME)

URL = 'ftp://ftp.ebi.ac.uk/pub/databases/gwas/releases/latest/gwas-catalog-associations_ontology-annotated.tsv'
PATH = os.path.join(DATA_DIR, 'gwas-catalog-associations_ontology-annotated.tsv')
