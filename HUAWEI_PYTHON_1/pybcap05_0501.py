# Escreva um programa que permaneça em laço enquanto um valor X lido for diferente de zero.
# Para cada valor de X apresente na tela se é par ou impar

# Temos de ter os Elementos do controle do laço que são
#  Situação inicial do controle
#  Condição de continuidade
# Alteração no objeto de controle a cada repetição


X= 1
while X != 0:
    X = int(input('Digite X: '))
    if X % 2 == 0:
        print(f'{X} é par')
    else:
        print(f'{X} é impar')

print('FIM')