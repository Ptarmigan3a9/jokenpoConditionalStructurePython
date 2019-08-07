from random import randint
from time import sleep

jogo = input('Informe pedra, papel ou tesoura:').lower()
if jogo == 'pedra':
    jogo = int(1)
elif jogo == 'papel':
    jogo = int(2)
elif jogo == 'tesoura':
    jogo = int(3)
else:
    print('Não fora informado pedra, papel ou tesoura!')
    exit()
n = randint(1, 3)
if jogo == 1 and n == 2:
    print('Papel!\nAha! Ganhei de você!')
elif jogo == 2 and n == 3:
    print('Tesoura!\nAha! Ganhei de você!')
elif jogo == 3 and n == 1:
    print('Pedra!\nAha! Ganhei de você!')
elif jogo == 1 and n == 3:
    print('Tesoura!\n...!!')
    sleep(1)
    print('\nPerdi! Lhe parabenizo!!!')
elif jogo == 2 and n == 1:
    print('Pedra!\n...!!')
    sleep(1)
    print('\nPerdi! Lhe parabenizo!!!')
elif jogo == 3 and n == 2:
    print('Papel!\n...!!')
    sleep(1)
    print('\nPerdi! Lhe parabenizo!!!')
else:
    print('Ops!\nParece que colocamos o mesmo sinal!! Vamos denovo!!')
