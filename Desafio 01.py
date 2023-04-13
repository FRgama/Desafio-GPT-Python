#Escreva um programa que calcule a média de três números digitados pelo usuário. O programa deve pedir que o usuário digite os três números, calcular a média e exibir o resultado na tela.
#Dica: Use a função input() para solicitar a entrada do usuário e a função print() para exibir o resultado.

escolha = float(input('escollha um numero: '))
escolha2 = float(input('escollha outro numero: '))
escolha3 = float(input('escollha mais um numero: '))
media = ((escolha + escolha2 + escolha3)/3)
print ('A média dos números {}, {} e {} escolhidos foi {:.2f}' .format(escolha, escolha2, escolha3, media))

