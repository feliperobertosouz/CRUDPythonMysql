import mysql.connector
from mysql.connector import Error
from create_db_connection import create_db_connection
from read_query import read_query

q1= """ 
    select COUNT(idUsuarios) from usuarios
"""
connection = create_db_connection("localhost","root","fek123","bdtestes")
results = read_query(connection,q1)

from_db = []

for result in results:
  result = list(result)
  from_db.append(result)
