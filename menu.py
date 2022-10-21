import PySimpleGUI as sg

#Criação da janela
def janelaMenu():
    sg.theme('Reddit')
    layout = [
    [sg.Button('Cadastrar Cliente')],
    [sg.Button('Visualizar Clientes')],
    [sg.Button('Atualizar Cliente')],
    [sg.Button('DESLOGAR')],
    [sg.Text('Você logou com sucesso', key='mensagemlogin')],
]
    return sg.Window('Menu', layout=layout, finalize=True)