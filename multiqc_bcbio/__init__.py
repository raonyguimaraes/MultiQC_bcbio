from __future__ import absolute_import

from .bcbio import MultiqcModule
from multiqc import config


# Add search patterns and config options for the things that are used in MultiQC_bcbio
def multiqc_bcbio_config():
    """ Set up MultiQC config defaults for this package """
    bcbio_search_patterns = {
        'bcbio/metrics': {'fn': '*_bcbio.txt'},
        'bcbio/coverage': {'fn': '*_bcbio_coverage.txt'},
        'bcbio/coverage_avg': {'fn': '*_bcbio_coverage_avg.txt'},
        'bcbio/variants': {'fn': '*_bcbio_variants.txt'},
        'bcbio/target': {'fn': 'target_info.yaml'},
        'bcbio/qsignature': {'fn': '*bcbio_qsignature.ma'},
        'bcbio/vcfstats': {'fn': '*_bcbio_variants_stats.txt'},
        'bcbio/seqbuster': {'contents': 'seqbuster'},
        'bcbio/umi': {'fn': '*_umi_stats.yaml'},
        'bcbio/viral': {'fn': '*viral*-counts.txt'},
        'bcbio/damage': {'fn': '*damage.yaml'},
    }
    config.update_dict(config.sp, bcbio_search_patterns)

    config.fn_clean_exts.append({'type': 'regex', 'pattern': '_bcbio.*'})
    
    config.update_dict(config.table_columns_visible, {
        'FastQC': {
            'percent_duplicates': False,
            'total_sequences': False,
        },
        'QualiMap': {
            'percentage_aligned': False,
        },
        'Samtools Stats': {
            'non-primary_alignments': False,
            'reads_mapped': False,
            'reads_mapped_percent': False,
            'raw_total_sequences': False,
        }
    })
