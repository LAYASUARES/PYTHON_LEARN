#classe set usada como Iterador

#Objetivo 1: Mostrar a questão da ordem dentro de um conjunto. Ordem essa que não consegue ser controlada, ou seja, é aleatória.
#Objetivo 2: Mostrar que os conjuntos podem ser usados em iterações com comando for, ou seja, são iteráveis.

print('primeira execução')
conjunto = {3.3, 18.6, 34.0, 43.1, 58.7}
for c in conjunto:
    print(c)

print('segunda execução')
conjunto = {18.6, 3.3, 58.7,34.0, 43.1}
for c in conjunto:
    print(c)


print('Fim do programa.')