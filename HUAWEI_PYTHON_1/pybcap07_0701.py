#Escreva um programa que leia 3 numeros inteiros:
#O primeiro termo P, a razão R e a quantidade Q de termos de uma progressão aritmica.
#O programa deve calcular os Q termos da progressão colocando-os em uma lista e no final exibi-la na tela.

#OBS: esse problea já foi abordado, sem o uso de listas, no exercicio resolvideo 5.3
# P=4
# R=3
# 4, 7, 10, 13, 16, 19, 22

P = int(input('Enter the primary term: '))
R = int(input('Enter the reason: '))
Q = int(input('Enter qtde of term: '))

Term = []
cont = 0

while cont < Q:
    Term.append(P)
    P = P + R
    cont += 1

print('List')
print(Term)
print('END')