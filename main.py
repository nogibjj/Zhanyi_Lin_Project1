from fastapi import FastAPI
import streamlit
import databricks
from databricks import sql
from pyspark.sql.types import *
import os
import pymysql
import pyodbc
from pyspark import SQLContext

with sql.connect(server_hostname = os.getenv("adb-3631385232028777.17.azuredatabricks.net"),
                 http_path       = os.getenv("/sql/protocolv1/o/3631385232028777/0914-175706-o6skpubi"),
                 access_token    = os.getenv("dapia7232804cbbf0edb101d38bfcfc60ba1-3")) as connection:

  with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM default.winemag_data LIMIT 2")
    result = cursor.fetchall()

    for row in result:
      print(row)

