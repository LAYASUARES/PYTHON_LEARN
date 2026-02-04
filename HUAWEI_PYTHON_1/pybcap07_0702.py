# Usando a classe range, escreva um programa que leia 3 numeros inteiros:
# O primiero temos P, a razão R e a quantidade Q de termos de uma progressão aritmetica.
# O programa deve calcular os Q termos da progressão colocando-os em uma lista e no final exibi-la na tela.

# OBS: è o mesmo enunciado que o exercicio 7.1

p = int(input('Digite um primeiro termo: '))
r = int(input('Digite a razão: '))
q = int(input('Digite a quantidade de termos: '))

ultimo = p + r * (q - 1) #regrade calcula, pesquisa qual é

#termos = list(range(start,stop, step)) - construção padrao e que precisamos disso em um range
termos = list(range(p, ultimo+1, r))

print('lista gerada')
print(termos)

