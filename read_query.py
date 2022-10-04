## Esse arquivo se trata de ler a query criada pelo sql, ele retorna uma lista de tuplas

import mysql.connector
from mysql.connector import Error

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")