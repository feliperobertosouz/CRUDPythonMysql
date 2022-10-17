## Esse arquivo faz a conexão com o banco de dados
import mysql.connector
from mysql.connector import Error

#Esse metodo cria a conexão com banco de dados de maneira simples sem ocupar espaço em toda pagina que é necessario essa conexão.
#Possui 5 parametros
#host_name: se trata do nome da host como ja dito
#user_name: nome do cadastro que sera usado para logar no banco de dados
#user_password: senha do usuario do banco de dados
#db_name: nome do banco de dados que será usado.
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection