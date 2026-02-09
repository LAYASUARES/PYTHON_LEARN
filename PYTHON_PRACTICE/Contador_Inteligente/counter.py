
numeros = []
A = 1

while A != 0:
     A= int(input('Digite um numero inteiro ou 0 para sair:'))
     numeros.append(A)
     
     
print(f'Temos {len(numeros)} de numeros totais')
print(f'A soma total entre eles é {sum(numeros)}')
print(f'Temos uma media de {sum(numeros)/len(numeros)}')
print(f'Aonde o maior valor é {max(numeros)} e menor {min(numeros)}')






