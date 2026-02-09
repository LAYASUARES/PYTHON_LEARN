Codigos = [103,117, 121, 135, 161, 189, 200, 204, 216]
Lista = []
print('Alternativa com if classico:')

# Algoritmo de filtro para colocar os numero de 200 para baixo Com if inline
for codigo in Codigos:
     if 120 <= codigo and codigo <= 200:
          Lista.append(codigo)
print(f'codigos filtrados --> {Lista}')

lista = []
for codigo in Codigos:
     lista.append(codigo) if 120 <= codigo and codigo<= 200 else None # assim podemos usar o inline sem o else sem consequencia nenhuma
print(f'codigos filtrados com if inline --> {lista}')
          