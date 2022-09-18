from fastapi import FastAPI
import databricks
from databricks import sql
from pyspark.sql.types import *
import os
import pymysql
import pyodbc
from pyspark import SQLContext
import requests
import json
import pandas as pd


def querydb(team1, team2):
    query="select date, tournament, home_team, away_team, home_team_score, away_team_score from default.historical_matches_csv where home_team = '%s' and away_team = '%s' or home_team = '%s' and away_team = '%s'" % (team1, team2,team2, team1)
    with sql.connect(server_hostname = os.getenv("DATABRICKS_SERVER_HOSTNAME"),
                 http_path       =  os.getenv("DATABRICKS_HTTP_PATH"),
                 access_token    = os.getenv("DATABRICKS_TOKEN")) as connection:

      with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        
    if team1 == team2:
        print("The same team, please input two different teams")
        return "The same team, please input two different teams"
    elif team1 == "Portugal" or team2 == "Portugal":
        print("The winner is: Portugal because of Cristiano Ronaldo")
        return "The winner is: Portugal because of Cristiano Ronaldo"
    elif team1 == "Brazil" or team2 == "France":
        print("The winner is: France because Benzema can be the new King of France")
        return "The winner is: France because Benzema can be the new King of France"
    else:
        df = pd.DataFrame(result)
        df.columns = ["date", "tournament", "home_team", "away_team", "home_team_score", "away_team_score"]
        print(df)
        return df
