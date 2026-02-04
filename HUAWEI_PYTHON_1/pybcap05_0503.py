# Escreva um programa que mostre na tela os 18 primeiros termos de uma progressâo aritmética (PA) com primeiro termo P e razaão R
# Os dois numeros P e R são inteiros e devem ser lidos do teclado.

P = int(input('Digite o primeiro termo: '))
R = int(input('Digite a razão: '))
cont = 1 # usarmos como nosso contador
while cont <= 10:
    print(P, end=', ')
    P = P + R
    cont = cont + 1 # cont += 1, mesmo coisa

print('FIM')