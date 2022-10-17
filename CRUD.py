import mysql.connector 
import PySimpleGUI as sg
from tabela import janelaInfo
from create_db_connection import *

#Conexão com banco de dados
connection = create_db_connection("localhost","root","fek123","bdtestes")
#Cursor = aquele que executara as querys
cursor = connection.cursor()

#Criação da janela
def janelaLogin():
    sg.theme('Reddit')
    layout = [
    [sg.Text('Usuario')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('Logar')],
    [sg.Text('Você ainda não tentou se conectar', key='mensagem')],
]
    return sg.Window('Login', layout=layout, finalize=True)



#Janela inicial
janela1,janela2 = janelaLogin(), None

#LOOP DE EVENTOS
while True:
    window, event,values = sg.read_all_windows()

    #window closed
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break
    if window == janela2 and event == sg.WINDOW_CLOSED:
        janela2.close()
    
    if window == janela1 and event== 'Logar':
        #Recebe valores do que foi digitado no text box 
        user = values['usuario']
        
        #O comando se trata da query que sera feita
        comando = f'SELECT Login From usuarios WHERE Login = "{user}"' #Seleciona da tabela login o login que corresponde ao que foi digitado
        #Executa o comando usando o cursor
        cursor.execute(comando)
        #Recebe o resultado da query executada anteriormente
        usuarioExiste = cursor.fetchall()

        #Se o valor recebido for diferente de vazio
        #Checa se o usuario existir
        if usuarioExiste != [] :
            
            #Altera o comando 
            #--- Executa o comando e recebe o resultado
            comando = f'SELECT Senha from usuarios Where Login = "{user}"' #Seleciona na tabela login o login achado e recebe a senha do usuario
            cursor.execute(comando)
            senhaBancoDeDados = cursor.fetchall()

            #Processo de transformar a query em uma string
            senhaBancoDeDados = senhaBancoDeDados
            senhaDigitada = values['senha']
            s = senhaBancoDeDados[0]
            senhaString = ''.join(s)

            #Se a senha digitada no campo for igual a senha buscada no campo, o login sera executado com sucesso
            if senhaString == senhaDigitada:
                #Abre a janela de informações com tabela, arquivo tabela.py
                janela2 = janelaInfo()
                window['mensagem'].update("LOGIN FEITO COM SUCESSO")
            else: #se a senha estiver errada
                print("SENHA ERRADA")
                window['mensagem'].update("SENHA OU USUARIO INCORRETO")
        else: # se o usuario não existir
            window['mensagem'].update("SENHA OU USUARIO INCORRETO")

#Para o cursor e a conexão para segurança
cursor.close()
connection.close()