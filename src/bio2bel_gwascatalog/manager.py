# -*- coding: utf-8 -*-

"""Manager for Bio2BEL GWAS Catalog."""

import logging
from typing import Mapping

import pandas as pd
from protmapper.api import hgnc_name_to_id
from tqdm import tqdm

from bio2bel import AbstractManager
from bio2bel.manager.bel_manager import BELManagerMixin
from pybel import BELGraph
from pybel.dsl import Gene, Pathology
from pybel.struct import count_functions
from .constants import MODULE_NAME
from .models import Base
from .parser import df_getter

__all__ = [
    'Manager',
]

logger = logging.getLogger(__name__)


def get_graph() -> BELGraph:
    df = df_getter()
    graph = BELGraph(
        name='GWAS Catalog',
        version='1.0.2',
    )
    graph.namespace_pattern.update(dict(
        dbsnp=r'^rs\d+$',
        efo=r'^\d{7}$',
        hgnc=r'^((HGNC|hgnc):)?\d{1,5}$',
    ))

    it = tqdm(df.values, desc='Mapping GWAS Catalog to BEL')
    for (
        pmid, mapped_gene, dbsnp_id, context, intergenic, minus_log_p_value, risk_allele_frequency,
        or_or_beta, confidence_interval, mapped_trait, mapped_trait_uri,
    ) in it:
        if pd.isna(mapped_trait_uri):
            continue

        annotations = dict(
            minus_log_p_value=minus_log_p_value,
            risk_allele_frequency=risk_allele_frequency,
            odds_ratio_or_beta=or_or_beta,
            confidence_interval=confidence_interval,
        )

        if pd.notna(context):
            annotations['gwascatalog_context'] = {c.strip() for c in context.split(';')}

        dbsnp_node = Gene(
            namespace='dbsnp',
            identifier=dbsnp_id,
        )
        pathology_node = Pathology(
            namespace='efo',
            name=mapped_trait,
            identifier=mapped_trait_uri.split('/')[-1][4:],
        )

        graph.add_association(
            dbsnp_node,
            pathology_node,
            citation=str(pmid),
            evidence=MODULE_NAME,
            annotations=annotations,
        )

        if intergenic in {'0', '0.0', 0, 0.0}:
            gene_symbols = [gene_symbol.strip() for gene_symbol in mapped_gene.split(',')]
            for gene_symbol in gene_symbols:
                hgnc_id = hgnc_name_to_id.get(gene_symbol)
                if hgnc_id is None:
                    continue
                    # TODO lookup for ensembl identifiers
                    # gene_node = Gene(
                    #     namespace='ensembl',
                    #     name=gene_symbol,
                    # )
                else:
                    gene_node = Gene(
                        namespace='hgnc',
                        identifier=hgnc_id,
                        name=gene_symbol,
                    )
                graph.add_has_variant(gene_node, dbsnp_node)
                graph.add_association(
                    gene_node,
                    pathology_node,
                    citation=str(pmid),
                    evidence=MODULE_NAME,
                    annotations=annotations,
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
        return True

    def summarize(self) -> Mapping[str, int]:
        """Summarize the contents of the Bio2BEL GWAS Catalog database."""
        return count_functions(self.to_bel())

    def populate(self) -> None:
        """Populate the Bio2BEL GWAS Catalog database."""

    def to_bel(self):
        if self.graph is None:
            self.graph = get_graph()
        return self.graph
