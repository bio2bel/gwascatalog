# -*- coding: utf-8 -*-

"""Manager for Bio2BEL GWAS Catalog."""

from typing import Mapping

import pandas as pd
from pybel import BELGraph
from pybel.dsl import Gene, Pathology
from tqdm import tqdm

from bio2bel import AbstractManager
from bio2bel.manager.bel_manager import BELManagerMixin
from .constants import MODULE_NAME
from .models import Base
from .parser import df_getter

__all__ = [
    'Manager',
]


def get_graph() -> BELGraph:
    df = df_getter()
    graph = BELGraph(
        name='GWAS Catalog',
        version='1.0.2',
    )
    it = tqdm(df.values, desc='Mapping GWAS Catalog to BEL')
    for pmid, mapped_gene, snps, context, intergenic, mapped_trait, mapped_trait_uri in it:
        if pd.isna(mapped_trait_uri):
            continue

        annotations = {} if pd.isna(context) else {
            'gwascatalog_context': {c.strip() for c in context.split(';')},
        }

        graph.add_association(
            Gene(
                namespace='dbsnp',
                identifier=snps,
            ),
            Pathology(
                namespace='efo',
                name=mapped_trait,
                identifier=mapped_trait_uri.split('/')[-1]
            ),
            citation=str(pmid),
            evidence='',
            annotations=annotations,
        )

        if intergenic == '0':
            genes = [g.strip() for g in mapped_gene.split(',')]
            for g in genes:
                graph.add_has_variant(
                    Gene(
                        namespace='dbsnp',
                        identifier=snps,
                    ),
                    Gene(
                        namespace='hgnc',
                        name=g,
                    ),
                )

    return graph


class Manager(AbstractManager, BELManagerMixin):
    """Manages the Bio2BEL GWAS Catalog database."""

    module_name = MODULE_NAME
    _base = Base

    def __init__(self, *args, **kwargs):
        self.graph = None

    def is_populated(self) -> bool:
        """Check if the Bio2BEL GWAS Catalog database is populated."""
        raise NotImplementedError

    def summarize(self) -> Mapping[str, int]:
        """Summarize the contents of the Bio2BEL GWAS Catalog database."""
        raise NotImplementedError

    def populate(self) -> None:
        """Populate the Bio2BEL GWAS Catalog database."""
        raise NotImplementedError

    def to_bel(self):
        if self.graph is None:
            self.graph = get_graph()
        return self.graph
