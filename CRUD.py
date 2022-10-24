from types import NoneType
import mysql.connector 
import PySimpleGUI as sg
from tabela import janelaInfo
from create_db_connection import *
from janelaLogin import janelaLogin, Logar
from menu import janelaMenu
from Cadastrar import *
from Atualizar import *
#Conexão com banco de dados
connection = create_db_connection("localhost","root","fek123","bdtestes")
#Cursor = aquele que executara as querys
cursor = connection.cursor()


#Janela inicial
janela2 = None
janela1 = janelaLogin()

#LOOP DE EVENTOS
while True:
    window, event,values = sg.read_all_windows()

    #window closed
    if event == sg.WINDOW_CLOSED:
        break
    
    ## JANELA DE LOGIN ##
    if window == janela1 and event== 'Logar':
        #Recebe valores do que foi digitado no text box 
        user = values['usuario']
        
        senhaDigitada = values['senha']

        logado = Logar(user,senhaDigitada,connection,cursor)

        if logado == True:
            janela1.close()
            janela1 = janelaMenu()
        else:
            window['mensagem'].Update("Falha ao logar")

    if window == janela1 and event== 'Cadastrar Cliente':
        janela1.close()
        janela1 = janelaCadastro()

    if window == janela1 and event== 'Visualizar Clientes':
        janela1.close()
        janela1 = janelaInfo()
    
    if window == janela1 and event== 'DESLOGAR':
        janela1.close()
        janela1 = janelaLogin()
    
    if  window == janela1 and event== 'Voltar':
        janela1.close()
        janela1 = janelaMenu()
    
    if window == janela2 and event== 'Voltar':
        janela2.close()
        janela1 = janelaMenu()

    if window == janela1 and event == 'Cadastrar':
        connection = create_db_connection("localhost","root","fek123","bdtestes")
        #Cursor = aquele que executara as querys
        cursor = connection.cursor()
        login = values['user']
        senhaCadastrar = values['password']
        sexCadastrar = values['sex']
        Cadastrar(login,senhaCadastrar,sexCadastrar,cursor,connection)
        Limpar(values,window)
        
        
    if window == janela1 and event ==  'Limpar':
        Limpar(values,window)

    if window == janela2 and event == 'Limpar':
        Limpar(values,window)
        window['id'].update(disabled = False)
        window['id'].update('')
        window['Pesquisar'].update(disabled = False)
        window['Excluir'].update(disabled = True, visible = False)
        window['user'].update(disabled = True)
        window['password'].update(disabled = True)
        window['sex'].update(disabled = True)
            
    if window == janela1 and event == 'Atualizar Cliente':
        janela1.close()
        janela2 = janelaAtualizar()

    if event == 'Pesquisar':
        id = values['id']
        checar = len(id)
        if(checar == 0):
             window['mensagem'].Update("Falha ao pesquisar")
        else:
            window['mensagem'].Update("")
            dados = Trazer(id)
            if len(dados) == 0:
                window['mensagem'].Update("Falha ao pesquisar")
            else:
                DefinirValores(window,dados)
                window['id'].update(disabled = True)
                window['Pesquisar'].update(disabled = True)
                window['Atualizar'].update(disabled = False)
                window['user'].update(disabled = False)
                window['password'].update(disabled = False)
                window['sex'].update(disabled = False)
                window['Excluir'].update(disabled = False, visible = True)

    if event == 'Atualizar':
        id = values['id']
        nome = values['user']
        senha = values['password']
        sexo = values['sex']
        connection = create_db_connection("localhost","root","fek123","bdtestes")
        #Cursor = aquele que executara as querys
        cursor = connection.cursor()

        Atualizar(connection,cursor,id,nome,senha,sexo)
        Limpar(values,window)

    if event == 'Excluir':
        connection = create_db_connection("localhost","root","fek123","bdtestes")
        #Cursor = aquele que executara as querys
        cursor = connection.cursor()
        id = values['id']
        Apagar(connection,cursor,id)
        Limpar(values,window)
        window['id'].update(disabled = False)
        window['id'].update('')
        window['Pesquisar'].update(disabled = False)
        window['Excluir'].update(disabled = True, visible = False)
        window['user'].update(disabled = True)
        window['password'].update(disabled = True)
        window['sex'].update(disabled = True)

cursor.close()
connection.close()