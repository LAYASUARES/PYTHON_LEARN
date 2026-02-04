#A = int(input('Digite A: '))
#B = int(input('Digite B: '))
#R = A / B
#print(R)

# Anwswer: Error - ZeroDivisionError: division by zero
# COmo proteger,ou seja, como fazer para não falhar, Ptra isso usamo try, except


A = int(input('Digite A: '))
B = int(input('Digite B: '))

try:
	R = A / B
	print(R)
except:
	print('Não é possivel calular a divisão')
print('FIM')
print('FIM')
print('FIM')