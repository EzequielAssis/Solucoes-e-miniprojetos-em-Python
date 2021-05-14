
# Jogo PEDRA, PAPEL, TESOURA (Jokempô)

from random import randint
from time import sleep

nome_result = ['  EMPATOU  ', 'VOCÊ PERDEU', 'VOCÊ GANHOU']
nome_esc = ['PEDRA', 'PAPEL', 'TESOURA']

# 0 ==> EMPATE
# 1 ==> VC PERDE
# 2 ==> VOCÊ GANHA

#   				   	     	| COMPUTER |

#  | U |                     pedra | papel | tesoura
#  | S |       pedra |    0      |    1      |     2      |
#  | E |       papel |    2      |    0      |     1      |
#  | R |   tesoura |    1      |    2      |     0      |

result = [[0, 1, 2],
    	        [2, 0, 1],
          	  [1, 2, 0]]

print('|| 1 - PEDRA   ||\n|| 2 - PAPEL   ||\n|| 3 - TESOURA ||\n')

esc_user = int(input('\ndigite sua escolha: '))
esc_computer = randint(1, 3)

#O usuário está acostumado a contar a partir de 1, mas o computador começa contar a partir do 0, portanto é necessário subtrair um 1, pois facilitará em acessar os índices das listas.
esc_user -= 1
esc_computer -= 1

if 0 <= esc_user <= 2:
	print('\n        JO !!!\n')
	sleep(1)
	print('        KEM !!!\n')
	sleep(1)
	print('        PÔ !!!\n')
	print('='*30)
	print(f'  VC JOGOU {nome_esc[esc_user]}')
	print()
	print(f'  O COMPUTADOR JOGOU {nome_esc[esc_computer]}')
	print('='*30)
	print()
	posicao = result[esc_user][esc_computer]
	#se invertermos as 'coordenadas' da matriz 		#para result[cumputer][user] devemos mudar a
	#lista nome_result[], tomando como referência 	#o resultado do computador.
	resultado = nome_result[posicao]
	print(f'-------- {resultado} ---------')

else:
	print('VC DIGITOU UMA OPÇÃO INVÁLIDA')
