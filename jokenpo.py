import random
from time import sleep
lista = ["SAIR    [0]", "PEDRA   [1]", "PAPEL   [2]" , "TESOURA [3]"]
def jogadas_pc():
  if pc == 1:
    print("o PC escolheu \033[35mpedra\033[0m")
  elif pc == 2:
    print("o PC escolheu \033[35mpapel\033[0m")
  else:
    print("o PC escolheu \033[35mtesoura\033[0m")

for c in range(0,4):
  print(lista[c])

while True:
  pc = random.randint(1,3)
  jogador = int(input("Escolha um número para a batalha: "))
  if jogador == 0:
    print("A batalha foi adiada... Volte quando quiser! ")
    break
  print("\033[34mJO\033[0m")
  sleep(1)
  print("\033[35mKEN\033[0m")
  sleep(1)
  print("\033[32mPÔ\033[0m")
  sleep(1)
  jogadas_pc()
  if pc == jogador:
    print("A batalha foi tensa... não há ganhadores, nem perdedores. ")
  elif jogador == 1:
    if pc == 2:
        print("Papel embrulha a pedra e a plateia vai a loucuuuura... \033[35mVocê perdeu!\033[0m")
    elif pc == 3:
        print("A batalha foi travada... Pedra, a mais indestrutível dos concorrentes com um único golpe quebrou a tesoura. \033[32mVocê ganhou!\033[0m")
  elif jogador == 2:
    if pc == 1:
      print("Papel embrulha a pedra e a plateia vai a loucuuuura... \033[33mVocê ganhou!\033[0m")
    elif pc ==3:
      print("o papel até tentou resistir... mas contra a mais afiada dos lutadores ele não da conta... \033[35mVocê perdeu!\033[0m")
  elif jogador == 3:
    if pc == 1:
       print("A batalha foi travada... Pedra, a mais indestrutível dos concorrentes com um único golpe quebrou a tesoura. \033[35mVocê perdeu!\033[0m")
    elif pc ==2:
      print("o papel até tentou resistir... mas contra a mais afiada dos lutadores ele não da conta... \033[33mVocê ganhou!\033[0m")
  print()
  import random
from time import sleep
lista = ["SAIR    [0]", "PEDRA   [1]", "PAPEL   [2]" , "TESOURA [3]"]
def jogadas_pc():
  if pc == 1:
    print("o PC escolheu \033[35mpedra\033[0m")
  elif pc == 2:
    print("o PC escolheu \033[35mpapel\033[0m")
  else:
    print("o PC escolheu \033[35mtesoura\033[0m")

for c in range(0,4):
  print(lista[c])

while True:
  pc = random.randint(1,3)
  jogador = int(input("Escolha um número para a batalha: "))
  if jogador == 0:
    print("A batalha foi adiada... Volte quando quiser! ")
    break
  print("\033[34mJO\033[0m")
  sleep(1)
  print("\033[35mKEN\033[0m")
  sleep(1)
  print("\033[32mPÔ\033[0m")
  sleep(1)
  jogadas_pc()
  if pc == jogador:
    print("A batalha foi tensa... não há ganhadores, nem perdedores. ")
  elif jogador == 1:
    if pc == 2:
        print("Papel embrulha a pedra e a plateia vai a loucuuuura... \033[35mVocê perdeu!\033[0m")
    elif pc == 3:
        print("A batalha foi travada... Pedra, a mais indestrutível dos concorrentes com um único golpe quebrou a tesoura. \033[32mVocê ganhou!\033[0m")
  elif jogador == 2:
    if pc == 1:
      print("Papel embrulha a pedra e a plateia vai a loucuuuura... \033[33mVocê ganhou!\033[0m")
    elif pc ==3:
      print("o papel até tentou resistir... mas contra a mais afiada dos lutadores ele não da conta... \033[35mVocê perdeu!\033[0m")
  elif jogador == 3:
    if pc == 1:
       print("A batalha foi travada... Pedra, a mais indestrutível dos concorrentes com um único golpe quebrou a tesoura. \033[35mVocê perdeu!\033[0m")
    elif pc ==2:
      print("o papel até tentou resistir... mas contra a mais afiada dos lutadores ele não da conta... \033[33mVocê ganhou!\033[0m")
  print()
  