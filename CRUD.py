import mysql.connector 
import PySimpleGUI as sg

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='fek123',
    database='bdtestes'
)
cursor = conexao.cursor()

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

def janelaInfo():
    sg.theme('Dark')
    layout2 = [
    [sg.Input('ID'), sg.Text('ABA DE PESQUISA')],
    [sg.Text('X')],
    [sg.Text('X')],
    [sg.Button('Pesquisar')],
]
    return sg.Window('Info', layout= layout2, finalize=True)

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

    if window == janela1 and event == 'Abrir':
        janela2 = janelaInfo()
    
    if window == janela1 and event== 'Logar':
        user = values['usuario']
        

        comando = f'SELECT Login From usuarios WHERE Login = "{user}"'
        cursor.execute(comando)
        usuarioExiste = cursor.fetchall()
        print(usuarioExiste)
        if usuarioExiste != [] :
            print("USUARIO EXISTE")

            comando = f'SELECT Senha from usuarios Where Login = "{user}"'
            cursor.execute(comando)
            senhaBancoDeDados = cursor.fetchall()
            senhaBancoDeDados = senhaBancoDeDados
            senhaDigitada = values['senha']
            s = senhaBancoDeDados[0]
            senhaString = ''.join(s)
            if senhaString == senhaDigitada:
                janela2 = janelaInfo()
                window['mensagem'].update("LOGIN FEITO COM SUCESSO")
            else:
                print("SENHA ERRADA")
                window['mensagem'].update("SENHA OU USUARIO INCORRETO")
        else:
            window['mensagem'].update("SENHA OU USUARIO INCORRETO")

cursor.close()
conexao.close()