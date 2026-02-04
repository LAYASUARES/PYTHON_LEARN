# Escreva um programa que leia um número inteiro Qtde e carrgue uma lista com ess quantidade de numeros inteiros aleatorios.
# Exiba a lista na tela
# Em seguida inicie uma laço que deve permanecer em execução enquanto um valor inteiro x for maior que zero.
# Para cada valor x verifique se ele está ou não na lista gerada
# Caso esteja é preciso exibir a quantidade de ocorrencias.

from random import randint #importação a biblioteca randint

#primeira parte
Lst = []
Qtde = int(input('Digite a quantidade: '))
for i in range(Qtde):
    a = randint(1, 20) # randint ela gera numeros aleatorios entre 2 limites
    Lst.append(a)

print('Lista gerada')
print(Lst)

#segunda parte
X = 1
while X > 0:
    X = int(input('Digite X: '))
    Lst.append(X)
    if X in Lst:
        print(f'   há {Lst.count(X)} ocorrências de {X} na lista')
    else:
        print(f'   {X} não está na lista')

print('END')