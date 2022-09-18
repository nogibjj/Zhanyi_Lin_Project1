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


def querydb(query="select date, tournament, home_team, away_team, home_team_score, away_team_score from default.historical_matches_csv where home_team = '%s' and away_team = '%s'" % ("Portugal", "Brazil")):
    with sql.connect(server_hostname = os.getenv("DATABRICKS_SERVER_HOSTNAME"),
                 http_path       =  os.getenv("DATABRICKS_HTTP_PATH"),
                 access_token    = os.getenv("DATABRICKS_TOKEN")) as connection:

      with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    
    return result
