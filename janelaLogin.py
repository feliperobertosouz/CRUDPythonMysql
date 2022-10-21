import PySimpleGUI as sg


#metodo Login
def Logar(user,senha,connection,cursor):
        
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
            senhaDigitada = senha
            s = senhaBancoDeDados[0]
            senhaString = ''.join(s)

            #Se a senha digitada no campo for igual a senha buscada no campo, o login sera executado com sucesso
            if senhaString == senhaDigitada:
                cursor.close()
                connection.close()
                return True
            else: #se a senha estiver errada
                return False
    else: # se o usuario não existir
        return False
        
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