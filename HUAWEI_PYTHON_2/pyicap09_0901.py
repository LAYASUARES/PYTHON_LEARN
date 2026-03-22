#Escreva um programa que leia um inteiro Qtde e crie um conjunto com lementos numéricos inteiros aleatórios dentro do intervalo fechado {1, 50}.
#Mostre o conjunto gerado na tela.
#Lembre-se que um conjunto não pode conter elementos repetidos, então a geração de numeros aleatórios pode representar um problema. Como resolver sisso?
#Cuidado: Este programa tem potencial para entrar em laço infinito caso o valor fornecido para Qtde seja maior do que 50. Façao teste e depois responda a pergunta: porque isso ocorre? 

from random import randint
Qtde = int(input("Digite a quantidade de elementos do conjunto: "))
conjunto = set()

while Qtde < 1 or Qtde > 50:
     print("Valor inválido. Digite um número entre 1 e 50.")
     Qtde = int(input("Digite a quantidade de elementos do conjunto (max 50): "))
     
while len(conjunto) < Qtde:
     conjunto.add(randint(1, 50))

print(conjunto)
print('')
print('Fim do programa.')