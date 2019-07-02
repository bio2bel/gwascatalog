# -*- coding: utf-8 -*-

"""Parsers and downloaders for Bio2BEL GWAS Catalog."""

from bio2bel.downloading import make_df_getter
from .constants import PATH, URL

__all__ = [
    'df_getter',
]

df_getter = make_df_getter(
    URL,
    PATH,
    sep='\t',
    usecols=[
        'PUBMEDID',
        'MAPPED_GENE',
        'SNPS',
        'CONTEXT',
        'INTERGENIC',
        'MAPPED_TRAIT',
        'MAPPED_TRAIT_URI',
    ]
)
