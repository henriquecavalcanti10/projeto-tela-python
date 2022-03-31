from PySimpleGUI import PySimpleGUI as sg # importando a bibli

 # layout
sg.theme('Reddit') # tema da janela
layout = [ # criando os layouts da tela
    [sg.Text('Usuário'),sg.Input(key='usuario')],
    [sg.Text('Senha),sg.Input(key='senha,passord_char'*')],
    [sg.Checkbox('Salvar o login')],
    [sg.Button('Entrar')]
]
 # janela
janela = sg.Windows('Tela de Login', layout)
 # ler os eventos
while True:
    eventos , valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'henrique' and valores['senha'] =='123456'
        print('Bem vindo')