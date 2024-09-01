import subprocess
import sys
import os
import PySimpleGUI as sg

def criar_ambiente_virtual(nome, diretorio=""):
    if not os.path.exists(nome):
        if diretorio:
            subprocess.run([sys.executable, '-m', 'venv', os.path.join(diretorio, nome)])
        else:
            subprocess.run([sys.executable, '-m', 'venv', nome])
        sg.popup_auto_close(f'Ambiente virtual "{nome}" criado com sucesso!')
    else:
        sg.popup_auto_close(f'A pasta "{nome}" já existe.')

def ativar_ambiente_virtual(nome):
    if os.path.exists(nome):
        if sys.platform == 'win32':
            subprocess.run([nome + '\\Scripts\\activate.bat'], shell=True)
        else:
            subprocess.run([f'source {nome}/bin/activate'], shell=True)
    sg.popup_auto_close(f'Ambiente virtual "{nome}" ativado.')

layout = [
    [sg.Text("Qual será o nome do seu ambiente virtual? ")],
    [sg.InputText(key='ambiente')],  
    [sg.Text("Onde quer que ele fique?"), sg.FolderBrowse(key='diretorio')],
    [sg.Button('Criar Ambiente', key='criar_ambiente'), sg.Button('Cancelar', key='cancel')]
]

sg.theme('BrightColors')

window = sg.Window('Criando Ambiente Virtual', layout, size=(400, 180))

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'cancel':
        break

    elif event == 'criar_ambiente':
        nome_ambiente = values['ambiente']
        diretorio = values['diretorio']
        criar_ambiente_virtual(nome_ambiente, diretorio)
        ativar = sg.popup_yes_no("Deseja ativar agora?")
        if ativar == "Yes":
            ativar_ambiente_virtual(nome_ambiente)
        else:
            sg.popup_auto_close('Ok, você pode ativá-lo depois. :)')

window.close()
