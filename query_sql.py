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
@click.option('--team2', default="Brazil", help='Number of greetings.')
def cli_query(team1, team2):
    """Input two teams for historical matches"""
    if team1 == team2:
        print("The same team, please input two different teams")
    elif team1 == "Portugal" or team2 == "Portugal":
        print("The winner is: Portugal")
    else:
        df = querydb.querydb("select * from default.historical_matches_csv where home_team = '%s' and away_team = '%s'" % (team1, team2))
        
        print(df)


# run the CLI
if __name__ == "__main__":
    cli()