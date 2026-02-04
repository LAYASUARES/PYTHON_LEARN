#Escreva um programa para exibir na tela o nome e a categoria de um lutador
#O programa deve ter um string para o nome e um numero real para o peso.
#Conforme o peso ocorrerá o enquadramento na categoria, segundo a tabela fornecida

Nome = input('Digite o nome: ')
Peso = float(input('Digite o seu peso: '))
if Peso < 52:
    Categoria = ''
elif Peso < 65:
    Categoria = 'Pena'
elif Peso < 72:
    Categoria = 'Leve'
elif Peso < 79:
    Categoria = 'Ligeiro'
elif Peso < 86:
    Categoria = 'Meio-médio'
elif Peso < 90:
    Categoria = 'Médio'
elif Peso < 100:
    Categoria = 'Meio-Pesado'
else:
    Categoria = 'Pesado'
msg = 'O lutador {} pesa {} kg e se enquadra na categoria {}'
if Categoria != '':
    print(msg.format(Nome, Peso, Categoria))
else:
    print(f'Peso invalido: {Peso}')
print('FIM')
