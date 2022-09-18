from cmd import PROMPT
import click
import querydb
# build  click commands for query directly
# build a click group
@click.group()
def cli():
#    """A simple CLI to query a SQL database"""
    "do something"


# build  click commands for query directly
@cli.command("WHO_WOULD_WIN")

@click.option('--team1', default="Portugal", help='Number of greetings.')
@click.option('--team2', default="China", help='Number of greetings.')
def cli_query(team1, team2):
    """Input two teams for historical matches"""
    
    querydb.querydb("select * from default.historical_matches_csv where home_team = '%s' and away_team = '%s'" % ("Bolivia", "Uruguay"))


# run the CLI
if __name__ == "__main__":
    cli()