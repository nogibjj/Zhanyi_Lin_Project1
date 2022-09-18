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
    with sql.connect(server_hostname = "adb-3631385232028777.17.azuredatabricks.net",
                 http_path       =  "sql/protocolv1/o/3631385232028777/0914-175706-o6skpubi",
                 access_token    = "dapi65bdbb392c0bf616660e12c2bd132b29-3") as connection:

      with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    
    return result
