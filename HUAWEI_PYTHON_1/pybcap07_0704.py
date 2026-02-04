# Escreva um programa que leia um número inteiro N.
# Em seguida leia N números inteiros carregando os valores negativos em uma lista e os positivos em outra
# Ao final exiba na tela cada uma das listas juntamente como seu tamanho

#OBS: Se o valor zero for fornecida ele deve ser incluida na lista de positivos.

n = int(input('Digite a qtde: '))
lneg = []
lpos = []
for i in range(n):  #aqui para garantir a interação em n valores
    x = int(input(f' elemento {i}: '))
    if x >= 0:
        lpos.append(x)
    else:
        lneg.append(x)

print(f' lista negativa: {lneg}')
print(f' lista positiva: {lpos}')

print('END')