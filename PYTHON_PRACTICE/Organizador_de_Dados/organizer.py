dados = []

for i in range(3):

     pessoas = {}
     nome = input("Digite o nome: ")
     idade = int(input("Digite a idade: "))
     cidade = input("Digite a cidade: ")
     
     pessoas["nome"] = nome
     pessoas["idade"] = idade
     pessoas["cidade"] = cidade
     
     dados.append(pessoas)
     
print(dados)
