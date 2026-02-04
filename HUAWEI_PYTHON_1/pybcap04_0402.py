#Escreva um programa que leia dois inteiros e mostre na tela apenas o menor dos dois
#Se ambos forem iguais,mostre qualquer um deles


A = int(input('Digite aqui o primeiro numero: '))
B = int(input('Digite aqui o segundo numero: '))

if A < B:
    print(f'O seu numero menor é {A}')
elif A == B:
    print(f'O seu numero menor é: {A}')
else:
    print(f'O seu numero menor é: {B}')

print('FIM')

