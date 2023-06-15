#Crie um programa que faça o computador jogar Jokenpô com você. Pedra, Papel e Tesoura.
#Use emojis representando uma mamão mostrando os símbolos.
from random import choice
opcoes = [1, 2, 3]
escolha = choice(opcoes)
print('\033[1;31m=-=\033[m' * 25)
print('Vamos jogar Jokenpô, escolha a sua jogada entre as seguintes opções: ')
print('\033[1;31m=-=\033[m' * 25)
print('1 = Pedra\n2 = Papel\n3 = Tesoura')
print('\033[1;31m=-=\033[m' * 25)
jogada = int(input('Qual será a sua jogada: '))
print('\033[1;31m=-=\033[m' * 25)
if escolha == 1:
    print('A minha escolha foi {} que é Pedra'.format(escolha))
elif escolha == 2:
    print('A minha escolha foi {} que é Papel'.format(escolha))
else:
    print('A minha escolha foi {} que é Tesoura'.format(escolha))
print('\033[1;31m=-=\033[m' * 25)
if jogada == escolha:
    print('\033[1;33mTente novamente, houve um empate!\033[m')
elif (jogada == 1) and (escolha == 2):
    print('Você perdeu, pois o papel cobre a pedra!')
elif (jogada == 2) and (escolha == 3):
    print('Você perdeu, pois a tesoura corta o papel!')
elif (jogada == 3) and (escolha == 1):
    print('Você perdeu, pois a pedra esmaga a tesoura!')
else:
    print('\033[1;34mParabéns você ganhou!\033[m')
print('\033[1;31m=-=\033[m' * 25)