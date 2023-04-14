#Crie um programa que leia uma lista de números inteiros e retorne a soma desses números. O programa deve continuar pedindo números para o usuário até que ele digite um número negativo. Ao final, o programa deve imprimir a soma dos números informados.

contador = 0
vezes = 0
while True:
    numero = float(input('Informe um número (informe um numero negativo para parar o programa): '))
    if numero < 0:
        break
    contador += numero
    vezes += 1
        
print('Desafio completo, voce colocou {} numeros e a soma dos números foi {}'.format(vezes, contador))
