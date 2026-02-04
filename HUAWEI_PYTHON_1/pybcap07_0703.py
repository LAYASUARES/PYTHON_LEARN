# Escreva um programa que leia um número inteiro N
# Em seguida leia N números reias carregando-os em uma lista
# Ao final exiba os elementos da lista na tela, sendo um em cada linha



n = int(input('Digite a qtde: '))

l =[]
for i in range(n):
    x = float(input(f' elemento {i}: '))
    l.append(x)

print('Resultado')
for valor in l:
    print(f' {valor: .2f}') # O .2f - serve para ele poder ler somente 2 numeros depois da virgula