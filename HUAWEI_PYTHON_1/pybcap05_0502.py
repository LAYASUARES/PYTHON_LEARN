# Escreva um programa que entre na tela a tabuada do número interiro M
# que deve ser lido do teclado


N = int(input('Digite N: '))
cont = 1
while cont <= 10:
    #R = cont * N  # Podemos fazer assim, ou como abariu pra não usar outro objeto
    print(f'{cont} x {N} = {cont*N}')
    cont = cont + 1

print('FIM')