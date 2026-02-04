#Escreva um programa que leia número interno e mostre na tela se ele é par ou impar.
#Lembrando que para saber a paridade de um inteiro é preciso calcular
#o resto da sua divisão por 2. Se o resto for 0 o numero é par
#se o resto for 1 o numero é impar


x = int(input('Digite um inteiro: '))
Resto = x % 2
if Resto == 0:
    print(f'O numero {x} é par')
else:
    print(f'O numero {x} é impar')

print('FIM')
