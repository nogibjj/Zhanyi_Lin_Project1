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

'''
with sql.connect(server_hostname = os.getenv("adb-3631385232028777.17.azuredatabricks.net"),
                 http_path       = os.getenv("/sql/protocolv1/o/3631385232028777/0914-175706-o6skpubi"),
                 access_token    = os.getenv("dapi2c9d6accb11f006ca6cb64c21e2b1794-3")) as connection:

  with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM default.winemag_data LIMIT 2")
    result = cursor.fetchall()

    for row in result:
      print(row)

'''



import os

from databricks_cli.sdk.api_client import ApiClient
from databricks_cli.clusters.api import ClusterApi

api_client = ApiClient(
    host=os.getenv("adb-3631385232028777.17.azuredatabricks.net"), token=os.getenv("dapi94b5cb5e464063238a25361e07e82cc7-3")
)

clusters_api = ClusterApi(api_client)
clusters_list = clusters_api.list_clusters()

print("Cluster name, cluster ID")

for cluster in clusters_list["clusters"]:
    print(f"{cluster['cluster_name']}, {cluster['cluster_id']}")