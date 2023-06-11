palavra='rato'.upper()
tentativas = []
chances = 5
ganhou=False
while True:
    for l in palavra:
        if l in tentativas:
            print(l,end=' ')
        else:
            print('_', end=' ')
    print(f'\nvocê tem {chances} chances')
    letra = input('escreva uma letra: ').upper()
    tentativas.append(letra)

    ganhou=True
    for j in palavra:
        if j not in tentativas:
            ganhou=False

    if letra not in palavra:
        chances = chances - 1

    if chances==0 or ganhou:
        break
if ganhou:
    print('Acertou!!!')
else:
    print('não foi dessa vez...')
print(f'a palavra era {palavra}')



