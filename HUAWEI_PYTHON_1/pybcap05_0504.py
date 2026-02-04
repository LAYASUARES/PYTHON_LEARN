# Escreva um programa que leia do teclado um número inteiro D.
# Esse numero deve ser obrigatoriamente maior.
# Em seguida exiba na tela todos os numeros inteiros menores que 100 e que sejam divisiveis por 0

D = int(input('Digite um numero inteiro: '))
if D < 0 :
    print(f'O valor {D} é invalido')
else:
    cont = 1
    while cont < 100:
        if cont % D == 0:
            print(cont)
        cont += 1


print('FIM')