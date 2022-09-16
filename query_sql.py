from cmd import PROMPT
import click
# build  click commands for query directly
@cli.command()

@click.option(
    "--query",
    default="SELECT * FROM default.winemag_data_2_csv LIMIT 2",
    help="SQL query to execute",
)