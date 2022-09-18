from cmd import PROMPT
import click
import querydb
import pandas as pd
import spark
import helpers
# build  click commands for query directly
# build a click group
@click.group()
def cli():
#    """A simple CLI to query a SQL database"""
    "do something"


# build  click commands for query directly
@cli.command("WHO_WOULD_WIN")

@click.option('--team1', default="Portugal", help='Number of greetings.')
@click.option('--team2', default="Brazil", help='Number of greetings.')
def cli_query(team1, team2):
    """Input two teams for historical matches"""
    df = pd.DataFrame(querydb.querydb(team1, team2))
    helpers.who_win(team1, team2, df)




# run the CLI
if __name__ == "__main__":
    cli()