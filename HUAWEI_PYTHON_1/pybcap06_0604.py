#A = int(input('Digite A: '))
#B = int(input('Digite B: '))

#try:
#	R = A / B
#	print(R)
#except:
#	print('Não é possivel calular a divisão')
#print('FIM')
#print('FIM')
#print('FIM')

# Se colocarmos uma letra ela vai dar um erro  ValueError: invalid literal for int() with base 10: '18O' que é um valor invalido
# para corrigirmos colocamos todo try na parte de cima pra proteger

try:
    A = int(input('Digite A: '))
    B = int(input('Digite B: '))
    R = A / B
    print(R)
except:
    print('ERRO Valor invalido')
print('FIM')

#ou colocar os error que pode ter

try:
    A = int(input('Digite A: '))
    B = int(input('Digite B: '))
    R = A / B
    print(R)
except ZeroDivisionError:
    print('O valor B não pode ser zero')
except ValueError:
    print('Digite numero inteiro para A e B')
except:
    print('Não é possivel calcular a divisão')
print('FIM')