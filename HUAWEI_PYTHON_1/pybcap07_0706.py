# Escreva um programa que permaneça em laço lendo numeros inteiros.
# O  laço termina quando for digitado o (zero).
# Cada valor diferente de zero digitado deve ser colocada em uma lista, desde que ele ainda não esteja lá, ou seja, valores repetidos não são aceitos.
# Se um valor repetida for digitado, o programa deve exibir uma mensagem na tela.
# Ao final exiba a lista e a quantidade de elementos que ele contém


LstValores = []
valor = int(input('Digite um valor inteiro: '))

while valor != 0:
    if valor not in LstValores: #Caso o valor não esteja ai sim faremos a inclusão se nã colocamos como erro
        LstValores.append(valor)
    else:
        print(f'   erro, o valor {valor} já esta na lista. ')
    valor = int(input('Digite um valor inteiro: '))

print('Resultados')
print(LstValores)
print(f'A lista contém {len(LstValores)} elementos')