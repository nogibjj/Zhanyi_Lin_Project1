#! /usr/bin/python
from cmd import PROMPT
import click
from requests import head
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
@cli.command("who_would_win")
@click.option('--team1', default="Portugal", help='Number of greetings.')
@click.option('--team2', default="Brazil", help='Number of greetings.')
def cli_query(team1, team2):
    """Input two teams for historical matches"""
    querydb.querydb(team1, team2)


@cli.command("histGame")
@click.option('--team1', default="Portugal", help='Number of greetings.')
def hisGame(team1):
    """Find the historical matches of a team"""
    print(querydb.hisGame(team1))

@cli.command("players")
@click.option('--team1', default="Portugal", help='Which team you want to check.')
def players(team1):
    """Input a team for players"""
    print(querydb.findPlayers(team1))

@cli.command("whichGroup")
@click.option('--team1', default="Portugal", help='Number of greetings.')
def whichGroup(team1):
    """Find the teams in the same group"""
    print(querydb.findGroup(team1))

@cli.command("recent")
@click.option('--team1', default="Portugal", help='See the recent news of a team')
def recent(team1):
    """See the recent news of a team"""
    links = querydb.recentNews(team1)
    for l in links:
        print(l)

# run the CLI
if __name__ == "__main__":
    cli()