from fastapi import FastAPI
import streamlit
import databricks
from databricks import sql
from pyspark.sql.types import *
import os
import pymysql
import pyodbc
from pyspark import SQLContext
import requests
import json


def querydb(query="SELECT * FROM default.winemag_data_2_csv LIMIT 2"):
    with sql.connect(server_hostname = "adb-3631385232028777.17.azuredatabricks.net",
                 http_path       =  "sql/protocolv1/o/3631385232028777/0914-175706-o6skpubi",
                 access_token    = "dapi65bdbb392c0bf616660e12c2bd132b29-3") as connection:

      with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    
    return result
