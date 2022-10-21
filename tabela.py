import mysql.connector 
import PySimpleGUI as sg
from create_db_connection import create_db_connection
from read_query import read_query

# Comando SQL usado para pesquisa da tabela, colocado em forma de variavel
q1= """ 
    select idUsuarios,Login,Sexo from usuarios
"""

#Usando o create_db_connection cria a conexão
connection = create_db_connection("localhost","root","fek123","bdtestes")
#Puxa o metodo de ler query para trazer o resultado da query
results = read_query(connection,q1)

from_db = []

#Faz um tratamento passando as informações da query lida que estão em TUPLE para uma LIST
for result in results:
  result = list(result)
  from_db.append(result)

#Definição da janela
def janelaInfo():
    sg.theme('Dark')
    #Definicação dos cabeçarios
    headings = ['ID', 'Login', 'Sexo']
    #Definição do layout da tabela
    layout = [
        [sg.Table(values= from_db,headings=headings,
        max_col_width =35,
        auto_size_columns=True,
        display_row_numbers=False,
        justification='right',
        key='-TABLE-',
        row_height=35
        )],
        [sg.Button('Voltar')]
        ]
    return sg.Window('Login', layout=layout, finalize=True)
