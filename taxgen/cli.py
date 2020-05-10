import click
import sys

from taxgen.inat_export import generate_tree as inat_generate_tree
from taxgen.ncbi_import import prepare_ncbi_taxdump
from taxgen.ncbi_export import generate_trees as ncbi_generate_trees
from taxgen.constants import DATA_DIR, EUKARYOTA_TAX_ID, INAT_OBSERVATION_FILE


def strip_url(ctx, param, value):
    """ If a URL is provided containing an ID, return just the ID """
    return value.split('/')[-1].split('-')[0] if value else None


@click.group()
def main():
    """ Main CLI entry point """


@main.command()
@click.option(
    '-i', '--input-file',
    default=INAT_OBSERVATION_FILE,
    show_default=True,
    type=click.Path(exists=True),
    help='CSV export file to read',
)
@click.option(
    '-o', '--output-dir',
    default=DATA_DIR,
    show_default=True,
    type=click.Path(),
    help='Directory to write output files to',
)
def inat(input_file, output_dir):
    """
    Read a CSV-formatted data export from iNaturalist and ouptut as a tree of keywords.
    A data export can be generated from the web UI here: https://www.inaturalist.org/observations/export
    """
    inat_generate_tree(input_file, output_dir)


@main.command()
@click.option(
    '-o', '--output-dir',
    default=DATA_DIR,
    show_default=True,
    type=click.Path(),
    help='Directory to write output files to',
)
@click.argument('root_nodes', nargs=-1)
def ncbi(output_dir, root_nodes):
    """
    Download and read NCBI taxonomy data and output as a tree of keywords.
    Optionally specify one or more taxon IDs to process only those taxa and their
    descendants. Defaults to Eukaryotes.
    """
    df = prepare_ncbi_taxdump()
    ncbi_generate_trees(df, output_dir, root_nodes or [EUKARYOTA_TAX_ID])
    # ncbi_generate_trees(df, [ANIMALIA_TAX_ID, PLANT_TAX_ID, FUNGI_TAX_ID])
