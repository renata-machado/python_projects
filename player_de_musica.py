from tkinter import *

# Configurações
janela = Tk()
janela.geometry("200x200")
janela.title("player de música")

# Criar um Frame para os botões
frame_botoes = Frame(janela)
frame_botoes.pack(side=BOTTOM, pady=15)

musica_atual = "música atual"

# Botoes
botao_play = Button(frame_botoes, text="<", command=0)
botao_play.pack(side=LEFT, padx=5)  

botao_prox = Button(frame_botoes, text="||", command=0)
botao_prox.pack(side=LEFT, padx=5) 

botao_antes = Button(frame_botoes, text=">", command=0)
botao_antes.pack(side=LEFT, padx=5)  

texto = Label(janela, text=musica_atual)
texto.pack(side=BOTTOM, pady=5)  

janela.mainloop()

