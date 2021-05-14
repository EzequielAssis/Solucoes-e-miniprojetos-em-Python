import random
import time
escolha = int(input('|| 1 - PEDRA ||\n|| 2 - PAPEL ||\n|| 3 - TESOURA ||\n\ndigite sua escolha: '))
stresc = 'PEDRA', 'PAPEL', 'TESOURA'
sorteio = random.randint(1,3)
result = [[0, -1, 1],
          [1, 0, -1],
          [-1, 1, 0]]

if escolha == 1 or escolha == 2 or escolha == 3:
    print('\nJÔ !!!\n')
    time.sleep(1)
    print('KEY !!!\n')
    time.sleep(1)
    print('PÔ !!!\n')
    escolha = escolha - 1
    sorteio = sorteio - 1
    print('VC JOGOU {}'.format(stresc[escolha]))
    print('O COMPUTADOR JOGOU {}'.format(stresc[sorteio]))

    if result[escolha][sorteio] == 0:
        print('----EMPATOU----')
    if result[escolha][sorteio] == 1:
        print('----VC GANHOU----')
    if result[escolha][sorteio] == -1:
        print('----VC PERDEU----')

else:
    print('VC DIGITOU UMA OPÇÃO INVÁLIDA')

