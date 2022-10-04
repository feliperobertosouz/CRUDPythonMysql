import mysql.connector 
import PySimpleGUI as sg
from create_db_connection import create_db_connection
from read_query import read_query


q1= """ 
    select idUsuarios,Login,Sexo from usuarios
"""
connection = create_db_connection("localhost","root","fek123","bdtestes")
results = read_query(connection,q1)

from_db = []

for result in results:
  result = list(result)
  from_db.append(result)


def janelaInfo():
    sg.theme('Dark')
    headings = ['ID', 'Login', 'Sexo']

    layout = [
        [sg.Table(values= from_db,headings=headings,
        max_col_width =35,
        auto_size_columns=True,
        display_row_numbers=False,
        justification='right',
        key='-TABLE-',
        row_height=35
        )]
        ]
    return sg.Window('Login', layout=layout, finalize=True)
