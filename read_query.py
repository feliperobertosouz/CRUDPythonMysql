## Esse arquivo se trata de ler a query criada pelo sql, ele retorna uma lista de tuplas

import mysql.connector
from mysql.connector import Error
#O read query recebe 2 parametros, conexão e a query
#Conexão: se trata da conexao com banco de dados, use o create_db_connection para alimentar a função
#Query, uma variavel String com comando sql
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")