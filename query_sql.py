from cmd import PROMPT
import click
import querydb
import pandas as pd
import spark
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
        print("The winner is: Portugal because of Cristiano Ronaldo")
    elif team1 == "Brazil" or team2 == "France":
        print("The winner is: France because Benzema can be the new King of France")
    else:
        df = pd.DataFrame(querydb.querydb("select date, tournament, home_team, away_team, home_team_score, away_team_score from default.historical_matches_csv where home_team = '%s' and away_team = '%s'" % (team1, team2)))
        df.append(querydb.querydb("select date, tournament, home_team, away_team, home_team_score, away_team_score from default.historical_matches_csv where home_team = '%s' and away_team = '%s'" % (team2, team1)))
        df.columns = ["date", "tournament", "home_team", "away_team", "home_team_score", "away_team_score"]
        team1_win = 0
        team2_win = 0
        for index, row in df.iterrows():
            if row['home_team'] == team1:
                if row['home_team_score'] > row['away_team_score']:
                    team1_win += 1
                else:
                    team2_win += 1
            else:
                if row['home_team_score'] > row['away_team_score']:
                    team2_win += 1
                else:
                    team1_win += 1

        print(team1 + " win " + str(team1_win) + " times")
        print(team2 + " win " + str(team2_win) + " times")

        if team1_win > team2_win:
            print("So, based on the historical matches, we predict that the winner is: " + team1)
        elif team1_win < team2_win:
            print("So, based on the historical matches, we predict that the winner is: " + team2)


# run the CLI
if __name__ == "__main__":
    cli()