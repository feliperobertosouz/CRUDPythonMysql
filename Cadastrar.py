import PySimpleGUI as sg
import mysql.connector

def Limpar(values,window):
    for key in values:
        window['user'].update('')
        window['password'].update('')
        window['sex'].update('')
    return None
    print("executado limpar")

def Cadastrar(usuario,senha,sexo,cursor,connection):  
    mycursor = cursor
    sql = "INSERT INTO usuarios (Login, Senha, Sexo) VALUES (%s, %s, %s)"
    val = (usuario,senha,sexo) 
    mycursor.execute(sql,val)
    connection.commit()
    print(mycursor.rowcount, "record inserted.")
    return(print("executado cadastrar"))



#Criação da janela
def janelaCadastro():
    sg.theme('Reddit')
    layout = [
    [sg.Text('usuario')],
    [sg.Input(key='user')],
    [sg.Text('Senha')],
    [sg.Input(key='password')],
    [sg.Text('Sexo')],
    [sg.Input(key='sex')],
    [sg.Button('Cadastrar'),sg.Button('Limpar')],
    [sg.Button('Voltar')]
]
    return sg.Window('Cadastrar', layout=layout, finalize=True)