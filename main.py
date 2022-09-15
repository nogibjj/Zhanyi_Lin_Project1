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
import keys


with sql.connect(server_hostname = "adb-3631385232028777.17.azuredatabricks.net",
                 http_path       = "sql/protocolv1/o/3631385232028777/0914-175706-o6skpubi",
                 access_token    = "dapi0e0f9e38fb26e69e9e26513cd7663b7f-3") as connection:

  with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM default.winemag_data_2_csv LIMIT 2")
    result = cursor.fetchall()

    for row in result:
      print(row)


print("connected")
app = FastAPI()