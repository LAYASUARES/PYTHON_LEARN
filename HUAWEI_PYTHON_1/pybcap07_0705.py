# Escreva um programa que permaneça em laço lendo numeros inteiros.
# O  laço termina quando for digitado o (zero).
# Cada valor diferente de zero digitado deve ser colocada em uma lista.
# Ao final exiba a lista na tela e a quantidade de elementos que ela contém

LstValores =[]

valor = int(input('Digite um valor inteiro: '))
LstValores.append(valor)
while valor != 0:
    LstValores.append(valor)
    valor = int(input('Digite um valor inteiro: '))

print('Resultado')
print(LstValores)

print(f'Alista contem {len(LstValores)} elementos')