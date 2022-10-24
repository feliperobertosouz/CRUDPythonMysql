import PySimpleGUI as sg
from create_db_connection import *
from read_query import *

def Trazer(id):

    connection = create_db_connection("localhost","root","fek123","bdtestes")
    #Puxa o metodo de ler query para trazer o resultado da query
    q1= f'Select * from usuarios where idUsuarios= {id}'

    results = read_query(connection,q1)

    from_db = []

    for result in results:
        result = list(result)
        from_db.append(result)
    return from_db
    
def DefinirValores(window,data):
    checar = len(data)
    if checar == 0:
        return False
    else:
        dados = data[0]
        window['id'].update('')
        window['user'].update('')
        window['password'].update('')
        window['sex'].update('')
    
        print(dados)
        id = dados[0]
        nome = dados[1]
        senha = dados[2]
        sexo = dados[3]
        window['id'].update(id)
        window['user'].update(nome)
        window['password'].update(senha)
        window['sex'].update(sexo)
        return True


def Atualizar(connection,cursor,id,nome,senha,sexo):
    mycursor = cursor
    val = nome,senha,sexo,id
    sql = "UPDATE usuarios set Login = %s, Senha = %s, Sexo = %s Where idUsuarios = %s"
    mycursor.execute(sql,val)
    connection.commit()
    cursor.close()
    connection.close()
    print("clicado no Atualizar")


def Apagar(connection,cursor,id):
    mycursor = cursor
    sql = f"delete from usuarios WHERE idUsuarios = {id}"
    mycursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()

def janelaAtualizar():
    sg.theme('Reddit')
    layout = [
    [sg.Text('usuario')],
    [sg.Input(key='user', disabled = True),sg.Text('ID:'),sg.Input(key='id')],
    [sg.Text('Senha')],
    [sg.Input(key='password', disabled = True)],
    [sg.Text('Sexo')],
    [sg.Input(key='sex', disabled = True)],
    [sg.Button('Atualizar', disabled = True),sg.Button('Pesquisar'),sg.Button('Limpar'),sg.Button('Excluir',disabled= True, visible = False, button_color=('white', 'red'))],
    [sg.Button('Voltar')],
    [sg.Text('',key='mensagem')]
]
    return sg.Window('Atualizar', layout=layout, finalize=True)