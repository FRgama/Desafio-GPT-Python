#Crie um programa que receba uma lista de números e retorne a média aritmética desses números. A lista deve ser fornecida pelo usuário e pode ter qualquer tamanho. Lembre-se de tratar o caso em que a lista estiver vazia.
vezes = 0
contador = 0
while True:
    numero = float(input('Digite um numero: (Para parar o programa digite 0) '))
    if numero == 0:
        break
    vezes += 1
    contador += numero
    media = contador/vezes
print('A quantidade de numeros selecionados foi {} e a soma deles foi {}, dito isso, a media dos numeros selecionados foi {:.2f} '.format(vezes, contador,media))