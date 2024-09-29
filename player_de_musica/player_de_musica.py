from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import os
from pygame import mixer

diretorio = ""
pasta_default = "player_de_musica/musicas" 
lista_musicas = []
indice_musica = 0
musica_atual = ""
tocando = False

def selecionar_arquivo():
    global diretorio, lista_musicas, indice_musica, musica_atual

    filetypes = (
        ('Arquivos MP3', '*.mp3'),
    )

    nome_do_arquivo = fd.askopenfilename(
        title='Selecione um arquivo',
        initialdir=os.path.normpath(pasta_default),
        filetypes=filetypes
    )
    
    if nome_do_arquivo:
        diretorio = os.path.dirname(nome_do_arquivo)
        musica_atual = os.path.basename(nome_do_arquivo)

        lista_musicas = [arquivo for arquivo in os.listdir(diretorio) if arquivo.endswith('.mp3')]
        lista_musicas = [os.path.join(diretorio, arquivo) for arquivo in lista_musicas] # caminho completo da musica
        
        try:
            indice_musica = lista_musicas.index(nome_do_arquivo)
        except ValueError:
            indice_musica = 0  

        atualizar_label()
        tocar_musica()

def atualizar_label():
    texto.config(text=musica_atual)

def prox_musica():
    global indice_musica, musica_atual, lista_musicas

    if lista_musicas:
        indice_musica = (indice_musica + 1) % len(lista_musicas)
        musica_atual = os.path.basename(lista_musicas[indice_musica])
        atualizar_label()
        tocar_musica()

def musica_anterior():
    global indice_musica, musica_atual, lista_musicas

    if lista_musicas:
        indice_musica = (indice_musica - 1) % len(lista_musicas)
        musica_atual = os.path.basename(lista_musicas[indice_musica])
        atualizar_label()
        tocar_musica()

def tocar_musica():
    global tocando, musica_atual, lista_musicas,indice_musica

    if lista_musicas:
        mixer.music.load(lista_musicas[indice_musica])
        mixer.music.play()
        tocando = True
        botao_play.config(text="||")

def pausar_musica():
    global tocando

    if tocando:
        mixer.music.pause()
        tocando = False
        botao_play.config(text="|>")

    else:
        mixer.music.unpause()
        tocando = True
        botao_play.config(text="||")

# Configuracoes 
mixer.init()
janela = Tk()
janela.geometry("300x200")
janela.title("Player de Música")

# Frame para os botoes
frame_botoes = Frame(janela)
frame_botoes.pack(side=BOTTOM, pady=15)

# Botoes
botao_anterior = Button(frame_botoes, text="<", command=musica_anterior)
botao_anterior.pack(side=LEFT, padx=5)

botao_play = Button(frame_botoes, text="|>", command=pausar_musica)
botao_play.pack(side=LEFT, padx=5)

botao_proxima = Button(frame_botoes, text=">", command=prox_musica)
botao_proxima.pack(side=LEFT, padx=5)

botao_selecionar_musica = ttk.Button(frame_botoes, text="Selecionar Música", command=selecionar_arquivo)
botao_selecionar_musica.pack(side=LEFT, padx=5)

# Exibe a música
texto = Label(janela, text="Nenhuma música selecionada")
texto.pack(side=BOTTOM, pady=5)

janela.mainloop()
