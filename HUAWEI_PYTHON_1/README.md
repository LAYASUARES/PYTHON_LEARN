# Notes
---

- **Print** - Comando pra poder mostrar no cmd e/ou uma resposta de algo armazenado em um objeto.
  ```c
  print()
  ```
  Por padrão ao colocar 2 ou mais valores no print ele deixa um espaço na resposta.
  ```c
  x = 26
  y = 58

  print(x, y)

  Resposta ou saida: 26 58
  ```
  Métodos usados juntos ao print:
  sep() - para alterar o separador automático, tipo colocar outra coisa invés do espaço em branco que for conveniente para si
  ```c
  x = 26
  y = 58

  print(x, y, .sep='-')

  Resposta ou saida: 16-58

  ou

  print(x, y, .sep=' - ')

  Resposta ou saida: 16 - 58
  ```
  format()
  ```c
  x = 26
  y = 58

  print('Valor de X = {0} e Y ={1}'.format(x, y)

  Resposta ou saida: Valores: X = 26 e Y = 58

  ou

  s1 = 'Valor de X = {} e Y ={}'.format(x, y)

  Resposta ou saida: Valor de X 26 e Y 58
  ```
  Sem format- método novo mais usado, podemos usar um dos dois pois dão a mesma resposta
  ```c
  s2 = 'Valor de X = {x} e Y ={y}'

  Resposta ou saida: Valor de X 26 e Y 58
  ```
  Sempre que colocamos os \ para colocar, eles fazem alguma especificação. EX:
  ```c
  print('um\ndois\ntrês')

  Resposta ou saida: um
                     dois
                     três

  print('um\tdois\ttrês')

  Resposta ou saida: um         dois         três
  ```
  Ou invés disso só usar o end() para separação e pular de linha
  ```c
  x = 26
  y = 58

  print( x, end='...')

  Resposta ou saida: 26...58

  print(y, end='\n')

  Resposta ou saida: 26
                     58
  ```

---

  - Ex de armazenamento de um valor em um objeto
  ```c
  qtde = 2
  puni = 5
  ```
  Aonde:
  - “=” - Comando de atribuição
  - “qtde” - Objeto
  - “2” - valor armazenado no objeto qtde

---

- **Type** - comando que pode ser usado pra mostra a classe que foi armazenada em um objeto

```c
type()
```

- Os tipos de classes são:
  - INT → Números inteiros
  - FLOAT → Números com virgula (números com casas decimais)
  - STR → String
  - BOOL → Booleano pode ser **True** ou **False**
  - NONE → Usado em algumas circunstâncias, ele representa que não tem nenhuma informação.
  Como armazenar ou converter o tipo de Classe para não aparecer ‘str’ quando colocado, pois inicialmente ele considera qualquer valor como String
  ```c
  N = input ('Digite um numero inteiro: ')
  Digite un numero inteiro: 37
  print (N)
  37

  F = input ('Digite um numero real: ')
  Digite um numero real: 31.47
  print (F)
  31.47

  R = N + F
  print (R)
  3731.47

  type (N)
  <class 'str'>

  type (F)
  <class 'str'>

  //Aqui ele ta reconhecendo como strings, inves de numeros mesmo pra isso só especificaramos as classes

  N = int(N)
  type (N)
  <class 'int'>

  F = float(F)
  type (F)
  <class 'float'>

  R = N + F
  print (R)
  68.47
  ```

---

- **Função Length** - ela mede o comprimento de um objeto composto.
  ```c
  d = len('exemplo')

  Resposta ou saida: 7
  ```
  Um objeto composto em Python é um objeto que contém referências a outros objetos. Em outras palavras, é um objeto cujos atributos ou elementos são, eles próprios, objetos.
  Ex:
  - **Classes e Instâncias de Classes**
  - **Listas**
  - **Tuplas**
  - **Dicionários**

---

- **Função ID** - está função ela pode ser usada para descobrirmos o id do objeto, ou seja, identificador numérico que vai funcionar nos bastidores.
  Esse id é usado pelo py para as suas tarefas internas, sendo ele um numero inteiro que é gerado automaticamente pelo py. E o desenvolvedor não tem controle sobre como ele será ou é.
  ```c
  obj1 = 10

  id(obj1) #comando
  140716878609112  #resposta do comnado id

  obj2 = 20

  id(obj2)
  140716878691234

  obj3 = 5 + 5

  id(obj3)
  140716878609112
  ```
  **Nota**: Não confunda ID com Identificador(Objeto) e se que 2 objetos diferentes tiverem o mesmo valor armazenado o seu ID será o mesmo. Sendo que eles estão apontando o mesmo id da memoria, que nem o obj1 e obj3

---

- **Funções de Biblioteca**
Pra usar uma biblioteca você tem de importar ela, pra isso você coloca assim
  
      ```c
      #Biblioteca matematica from math import sqrt #aqui só importa a função sqrt da biblioteca math

                ou

      import math   #aqui importa a biblioteca inteira todas funções
      ```

      Dentro dessa) biblioteca temos várias funções que podemos usar
      EX: Qdo usamos a primeira importação

      ```c
      from math import sqrt

      X = 49
      R = sqrt(x)  # função pra achar a raiz quadrada
      ```

      EX: Qdo usamos a segunda importação

      ```c
      import math

      x= 49
      math.sqrt(x)   # aqui temos sempre de fazer referencia ao nome da biblioteca como prefixo

      ```

      https://docs.python.org/3/ - Procurar aqui na seção de importar as bibliotecas e suas funções

---

- **Função Input** - Entrada de dados.
  Tem como objetivo fazer a leitura do teclado e o que for digitado ela retorna pra ser carregado em um objeto que nós especificamos aqui numa operação de atribuição.
  ```c
  A = input() # inicialmete só assim não faz nada temos de digitar algum valor
  Digite algo  #Esse valor foi armazenado no objeto A

  print(A)

  Resposta ou saida: Digite algo

  ```
  Assim fica estranho, por isso que o input é muito usado pra questão aonde tem de colocar um valor para ser armazenado, por ex qdo precisamos de informações do usuário
  ```c
  A = input('Digite algo: ')

  Digite algo:   #Aqui o user escreve o valor
  Digite algo: 8  #essa parte n aparece é só pra dar um exemplo

  print(A)

  Resposta ou saida: 8

  ```
  EX: Num caso normal e mais pratica com resposta int inves de ser uma str
  ```c
  A = input ('Digite um numero inteiro: ')
  Digite un numero inteiro: 12
  print (A)
  12

  type(A)
  <class 'str'>

  A = int(A)
  type(A)
  <class 'int'>

  //Inves disso tudo podemos fazer assim

  B = int(input ('Digite um numero inteiro: '))
  Digite un numero inteiro: 8
  type(B)
  <class 'int'>

  A * B
  696

  E

  F = float(input ('Digite um numero real: '))
  Digite um numero real: 5.3
  type(F)
  <class 'float'>
  ```
  Nota: Cuidado ao usar dessa forma pois se na resposta for necessário colocar um outro tipo de valor de classe diferente daquela que está presente vai dar um erro

---

- **Condicional** - comando que é usado e existe pois por x’s em algoritmo vamos ter ou remos precisar de vais opções do que vai acontecer ou não.

  ```c
  A = 0
  B = 10

  R = B / A

  //Ira dar um erro se fizermos essa divisão,então precisamos de um comando pra que se der erro apresente outra coisa

  A = int(input('Digite A: '))
  B = int(input('Digite B: '))

  if B == 0:
    print('Não é possivel calcular a divisão')
  else:
    R = A / B
    print(R)


    //Aqui ele pergunta e faz ocalulo e apresenta a mensagem qdo fordar erro
  ```

  Tipos de condições ou operadores de comparação que pode ser usado:

  - == igualdade
  - '<>' ou '!=' - **Verificar se dois valores não são iguais**
  - '>' - **Maior que: Comparar grandezas numéricas**
  - '<' - **Menor que: Comparar grandezas numéricas**
  - '≥' - **Maior ou igual a: Comparar grandezas numéricas, incluindo o próprio valor limite**
  - '≤' - **Menor ou igual a: Comparar grandezas numéricas, incluindo o próprio valor limite**

  - Condições simples - tipo A > B = True or False
  Condições compostas - tipo A > 0 and B < 0 = True or False
  A > 0 or B < 0 = True or False
      ## 1. Tabela de Verdade para `and` (E)

      O operador **`and`** retorna `True` (Verdadeiro) **apenas** se **ambos** os operandos forem `True`. Caso contrário, retorna `False`.

      | **Operando 1 (A)** | **Operando 2 (B)** | **Resultado (A and B)** |
      | --- | --- | --- |
      | `True` | `True` | `True` |
      | `True` | `False` | `False` |
      | `False` | `True` | `False` |
      | `False` | `False` | `False` |

      ## 2. Tabela de Verdade para `or` (OU)

      O operador **`or`** retorna `True` (Verdadeiro) se **pelo menos um** dos operandos for `True`. Retorna `False` **apenas** se **ambos** os operandos forem `False`.

      | **Operando 1 (A)** | **Operando 2 (B)** | **Resultado (A or B)** |
      | --- | --- | --- |
      | `True` | `True` | `True` |
      | `True` | `False` | `True` |
      | `False` | `True` | `True` |
      | `False` | `False` | `False` |

      ## 3. Tabela de Verdade para `not` (NÃO)

      O operador **`not`** inverte o valor booleano do operando. Se o operando for `True`, ele retorna `False`, e vice-versa.

      | **Operando (A)** | **Resultado (not A)** |
      | --- | --- |
      | `True` | `False` |
      | `False` | `True` |

      ```c
      A = True
      B = False

      print(not A)  # Saída: False
      print(not B)  # Saída: True
      print(not 5)  # Saída: False (5 é 'Truey', então inverte para 'False')
      print(not 0)  # Saída: True (0 é 'Falsey', então inverte para 'True')
      ```

      Resumo dos Operadores Lógicos em Python

      | **Operador** | **Significado** | **Descrição** |
      | --- | --- | --- |
      | `and` | E | Retorna `True` se ambos os lados são `True`. |
      | `or` | OU | Retorna `True` se pelo menos um lado é `True`. |
      | `not` | NÃO | Inverte o valor booleano do operando. |

      Você pode combinar tudo isso para formar condições complexas, como:

      ```c
      idade = 20
      tem_carteira = True

      if (idade >= 18) and (tem_carteira == True):
          print("Pode dirigir")

      # O 'not' também pode ser usado assim:
      if not tem_carteira:
          print("Não pode dirigir, não tem carteira")
      ```

Nota: o **AND** é prioridade de execução entre ele e o **OR,** ou se tiver parênteses o que estiver dentro dele, sera feito primeiro

---

- **Comando de Repetição** - comando usado pra podermos repetir um determinado número de vezes uma sequencia de comandos do programa, esse processo chamamos de laço ou loop.

  Aonde usamos a questão de Incremento e decremento

  - Incremento

  ```c
  A = 10
  A = A + 1  #Incremento que em resposta é igual a 11

  A += 1 #Mesma coisa que o de cima mas simplificado

  P = 4
  A += P # isso equivale a A = A + P, resultado 14
  ```

  - Decremento

  ```c
  A = 10
  p = 4
  A -= P isso equivale a A = A - P, resultado 6
  ```

  ```c
  #Inves de nós colocar a repetição, repetinos ela uma de cade vez

  cont = 1
  print(cont)

  cont = cont + 1  //Assim aqui sempre ira contar o valor de cont acima + 1, ou seja, aumentara sempre um
  print(cont)

  cont =  cont + 1
  print(cont)

  cont =  cont + 1
  print(cont)

  #Resposta que ira dar:
  1
  2
  3
  4
  ```

  Invés dessa repetição usamos o comando de função laço while()

  ```c
  cont = 1
  while cont <= 4:  //Ou seja, enquanto cont for <= a 4 repita a sequecnia a baixo, assim quando chegar a 4 ele para
  print(cont)
  cont =  cont + 1

  ```

  ```c
  # Para podermos ter um comando de repetição correto precisamos prestar atenção em 4 pontos

  cont = 1  //1- Ter uma situação inicial
  while cont <= 4:  //2- Ter uma condição de continuidade do laço
  print(cont)  //4- Ter a tarefa a ser repetida
  cont =  cont + 1 //3- Ter uma ação que é feita a cada repetição sobre o controle do laço

   #Esses 3 elementos formam um laço de repetição
  ```

  Nota: Tendo em conta o comando a condição é colocada, o programa só irá parar assim que o valor da condição mudar, ou seja, enquanto os valores que aparecerem forem ≤ a 4 ele são verdadeiros e o programa continua, se for fora dessa condição o valor é falso enquanto logo no primeiro falso o programa para.

  - **Comando Continue** - no Python serve para **pular o restante do código dentro de um loop** e passar direto para a próxima repetição (iteração).

  Ele não encerra o loop (como o `break`), apenas ignora o que vem depois dele naquele ciclo específico.

  ```c
  for i in range(5):
      if i == 2:
          continue  # Quando i for 2, ele pula o print abaixo
      print(i)
  ```

  **Resultado:**`0, 1, 3, 4` (o número 2 foi ignorado).

  - **Comando Break** - serve para **interromper e sair do loop imediatamente**, não importa quantas repetições ainda faltavam.
  Enquanto o `continue` apenas pula uma etapa, o `break` "quebra" a estrutura e encerra a execução do laço de repetição.
  ```c
  for i in range(10):
      if i == 3:
          break  # Quando i for 3, o loop para totalmente
      print(i)
  ```
  **Resultado:**`0, 1, 2` (o loop foi encerrado assim que chegou no 3).

### Resumo da diferença:

- **Continue:** Pula para a próxima volta.
- **Break:** Para tudo e sai do loop.

---

- **Try, Except** - tipo de construção que existe, py e outras linguagens para tratar erros que eventualmente possam acontecer.
  ```c
  A = int(input('Digite A: '))
  B = int(input('Digite B: '))

  try:
  	R = A / B
  	print(R)
  except:
  	print('Não é possivel calular a divisão')
  ```
  Try - conjunto de código, que vai ser protegido caso algum erro ocorra o except é conjunto de código que ira tratar a ocorrência do erro

---

- **Lista - Classe** - uma coleção de objetos
  Ele é declarado da seguinte forma:
  ```c
  L = []  #Lista vazio

  L = [44, 17, 15, 36] #Lista com 4 valores
  ```
  **Nota**: na lista temos o que chamamos de Objeto mutável, ou seja, este tipo de objeto pode ter os seus elementos alterados que o seu ID não mudara. Nesse caso o L que tem todos os números armazenados.
  Objeto Imutável - a alteração de conteúdo implica na alteração do ID numérico do objeto.
  Objeto Imutável - a alteração de conteúdo ocorre sem a alteração do ID numérico do objeto.
  ![image.png](attachment:f8a16ed8-ee98-4b60-8612-0727504802f3:image.png)
  ***
  A contagem de elementos ou como chamamos Indices já sabes começa sempre com zero
  Ex: Usando o L = [44, 17, 15, 36]
  ```c
  L = [44, 17, 15, 36]
       0    1   2   3
  ```
  - Listas - Classe list com ela criamos objetos compostos, ou seja, um objeto que contem outros objetos dentro dele

  ```c
  L = [11, 55, 88, 86, 45, 25, 85]
  ```

  Assim conseguimos acessar individualmente, seus elementos através do índice, podemos manipula eles como um todo ou individualmente.

  Imaginemos que temos uma lista grande que não sabemos o tamanho, podemos simplesmente colocar o comando len pra saber o seu tamanho

  ```c
  print(len)  # resposta será 6

  print(L[1]) # resposta será 11, pois o primeiro elemento é 11

  print(L[-1]) # resposta será 25, pois de tras pra frente ele é o primeiro

  //Outra podemos manipular elas de forma que se colocarum objeto tendo em conta a sua len, ou seja sua posição

  i = 3

  print(L[i+ 1]) # resposta será 45, pq 3+1=4, e o numero na posição 4 é o 45
  print(L[i- 1]) # resposta será 88
  print(L[i* 2]) # resposta será 85
  ```

  - para adicionar um novo elemento a lista colocamos o comando append
  ```c
  L.append(71)

  # respota será
  # [11, 55, 88, 86, 45, 25, 85, 71]
  ```
  - E pra remover a função del
  ```c
  del L[6]

  # resposta será
  # [11, 55, 88, 86, 45, 25, 85]

  ```

E para alterar um elemento existem somente colocar um por cima mesmo

  - Fatiamento - Podemos fazer o fatiamento pra pegar somente determinadas partes da lista somente

  ```c
  L = [11, 55, 88, 86, 45, 25, 85]

  Destino = L[3:5]

  # ira aprensentar os numeros da posição 3 até a posição 6
  # ou seja - [86, 45, 25]

  Destino1 = L[:4] # do 4 em diante
  # resposta - [11, 55, 88, 86]

  Destino2 = L [:]
  # aqui armazena amesma lista com ID diferente
  ```

  - Métodos na Classe List
    - **append** -para colocar elementos a uma lista, sempre vao ser colocados no final da lista. L.append()
    - **clear** - Para retirar todos elementos da lista . L.clear()
    - **copy** - retorna uma copia da lista, tem de ser colocado em outro objeto. A = L.copy()
    - **count** - Conta quantos elementos de um determinado valor existe dentro de uma lista. L.count()
  ```c
  L = [11, 55, 88, 85, 45, 25, 85]

  L.count(11)
  # resposta = 1, pois só tem o numero 11 uma vez

  L.count(85)
  # resposta = 2, pois tem 2 desses numeros na lista
  ```
    - **extend** - usada quando tem duas listas, ele ajuda a extender os elementos de uma lista para outra, ou seja, ele pega os elementos de uma lista e coloca no outro sem que a lista adicional se altere
  ```c
  L = [11, 55, 88, 85, 45, 25, 85]
  A = [1, 2, 3, 4]

  L.extend(A)
  # resposta = [11, 55, 88, 85, 45, 25, 85, 1, 2, 3, 4]
  ```
    - **index** - ele retorna o índice de um determinado valor, ou seja, a sua posição na lista. L.index() - no parenteses coloca o numero pra ver se está na lista
  ```c
  L = [11, 55, 88, 85, 45, 25, 85]

  L.index(55)
  # resposta = 2, pois esta a posição 2
  ```
  **Nota:** um cuidado com index, é que não sabemos dos elementos que estão na lista, pois se tentarmos um valor que não esta na lista vai dar erro, ou seja, não podemos usar o index quando um elemento não esta na lista
  Ai surge a questão como podemos ver se o ele elemento esta na lista ou? não pra isso usamos o operador in
  ```c
  L = [11, 55, 88, 85, 45, 25, 85]

  55 in L
  # resposta = True

  42 in L
  # resposta = False

  ```
    - **insert** - inclusão de elementos na lista, que nem o append(mas ele só coloca no final da lista), já o insert da para colocar em qualquer posição da lista
  ```c
  L = [11, 55, 88, 85, 45, 25, 85]

  L.insert(1, 76) #o 1 corresponde a posição aonde queremos e o 76 o valor que queremos colocar
  # resposta = [11, 76, 55, 88, 85, 45, 25, 85]

  ```
  Aqui se tentar colocarmos um valor em alguma posição que seja maior na lista ele simplesmente colocará no final da lista como emum append
    - **pop** - ele remove um elemento da lista, temos de colocar oposição e tem de ser armazenado.A = L.pop(), e por padrao ele retira sempre o ultimo se não especificarmos a posição
    - **remove** - ele remove pelo valor, ou seja, quado já sabemos o valor. L.remove()
    - **reserve** - ele inverte a lista literalmente. L.reserve()
    - **sort** - ele faz a classificação da lista de forma crescente, ou seja, coloca organizada de forma crescente. L.sort()

---

- **Comando For** - comando usado pra criação de laços de repetição de uso especifico, chamamos de iteradores.
  Ele faz um processo de repetição e em cada repetição o objeto de controle recebe um elemento de lista array, etc e pode usar esse elemento para todo e qualquer processamento que se faça necessario
  ```c
  L = [11, 55, 88, 85, 45, 25, 85]

  for valor in L:
  	print(valor)
  ```
  Neste exemplo estão usando listas , mas podemos colocar todo ou qualquer objeto composto como: listas, tuplas, strings, dicionarios, conjuntos, arrays; todos eles podem utilizados como iteraveis no comando FOR
