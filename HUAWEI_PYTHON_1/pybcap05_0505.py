# Escreva um program que permaneça elaço enquanto um valor inteiro lido for difeente de 0.
# Totalize e conte os valores digitados, exceto o zero, e apresente esses valores na tela.
# Totalizar é somar os valores

Soma= qte = 0
A = 1
A = int(input('Digite um valor: '))
while A != 0:
    Soma = Soma + A
    qte = qte + 1
    A = int(input('Digite um valor: '))
print(f' Soma dos Valores {Soma}')
print(f' Quantidade de Valores {qte}')
print('FIM')
