#Crie um programa que faça o computador jogar Jokenpô com você. Pedra, Papel e Tesoura.
#Use emojis representando uma mamão mostrando os símbolos.
import emoji
from random import choice
from time import sleep 
opcoes = [1, 2, 3]
escolha = choice(opcoes)
print('\033[1;31m=-=\033[m' * 25)
nome = str(input('Como é o seu nome? '))
print('Que tal nós jogarmos Jokenpô {}?'.format(nome))
print('Escolhe um número que equivale a sua jogada entre as seguintes opções: ')
print('\033[1;31m=-=\033[m' * 25)
print('1 = Pedra {}\n2 = Papel {}\n3 = Tesoura {}'.format(emoji.emojize(":oncoming_fist:"), emoji.emojize(":raised_back_of_hand:"), emoji.emojize(":victory_hand:")))
print('\033[1;31m=-=\033[m' * 25)
jogada = int(input('Qual será a sua jogada: '))
print('\033[1;31m=-=\033[m' * 25)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('\033[1;31m=-=\033[m' * 25)
sleep(1)
if escolha == 1:
    print('A minha escolha foi Pedra {}'.format(emoji.emojize(":oncoming_fist:")))
elif escolha == 2:
    print('A minha escolha foi Papel {}'.format(emoji.emojize(":raised_back_of_hand:")))
else:
    print('A minha escolha foi Tesoura {}'.format(emoji.emojize(":victory_hand:")))
print('\033[1;31m=-=\033[m' * 25)
if jogada == escolha:
    print('\033[1;33mTente novamente, houve um empate!\033[m')
elif (jogada == 1) and (escolha == 2):
    print('\033[1;35mJogador perde, pois o papel cobre a pedra!\033[m')
elif (jogada == 2) and (escolha == 3):
    print('\033[1;35mJogador perde, pois a tesoura corta o papel!\033[m')
elif (jogada == 3) and (escolha == 1):
    print('\033[1;35mJogador perde, pois a pedra esmaga a tesoura!\033[m')
else:
    print('\033[1;34mParabéns você ganhou!\033[m')
print('\033[1;31m=-=\033[m' * 25)

