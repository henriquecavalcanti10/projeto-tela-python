import PySimpleGUI as sg

layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Text('',key='mensagem')],
]

window = sg.Window('login', layout=layout)

while True:
    eventos, valores = window.read()
    if eventos == sg.WIN_CLOSED:
        break
    elif eventos == 'login':
        senha_correta = '123456'
        usuario_correto = 'henrique'
        usuario = valores ['usuario']
        senha = valores ['senha']
        if senha == senha_correta and usuario == usuario_correto:
            window['mensagem'].update('Login feito com sucesso !')
        else:
            window['mensagem'].update('Login e senha incorretos !')