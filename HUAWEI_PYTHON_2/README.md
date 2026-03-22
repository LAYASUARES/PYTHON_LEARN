# NOTES
---
    
 -   **Comando match-case** - Comando condicional múltiplo
    
    Estrutura:
    
    ```c
    n = -1
    
    while n != 0:
        n = int(input("Digite um número inteiro (0 para sair): "))
        match   n:                                                  #aqui coom o match colocamos o objeto que será usado nas comparações
              case 1:                                             # aqui podemos colocar quantas cases para podermos resolver um determinado problema
               print("Você digitou um.")
            case 2:
                   print("Você digitou dois.")
            case 3:
                   print("Você digitou três.")
            case _:                                     #clasula default, para nenhuma seja resolvida
    ```
    

O **match-case** tem essa característica ele compara o conteúdo do que foi colocado, com cada uma das parcelas cases. E não importa a ordem dos cases eles serão sempre executados da mesma forma, pois não interfere no match-case.

Já o case_: não pode nem ser o primeiro e nem ser o ultimo

---

- **Condicional if** que é escrito em uma unica linha mais conhecido como  **If inline**

EX: **Inves de**

```c
X = 10
Y = 9
if X >= Y:
  print(X) #unico comando
else:
  print(Y) #unico comando
```

Ele fica assim:

```c
print(X) if X >= Y else print(Y)
```

Aqui ele abre com aquilo que eu faço primeiro print(X)  quando der verdadeiro e ele fecha quando der Falso, e no meio da construção temos a condição.

Nota: nessa construção **inline** o **else** é obrigatório colocar e não usamos o “:”, ou seja, **If inline** podemos usar desde que seja completo e somente quando tiver um único comando na parte do else e na parte do if

---

- **Classe Set** - **Conjuntos em Python → serve para criarmos conjuntos em Py**

Na criação de conjuntos existem 2 modos:

  - 1ª Modo - Criar um conjunto com conteúdo, ou seja, ele nasce já contendo conteúdo

```c
C = {15, 4, 56, 7, 58, 69}
type(C)

#Resposta do type
<classe 'set'>

C3 = set( 4, 67, 59, 2) #Se colocar assim, vai dar sempre erro, pois assim com set(), aceita somente um argumento
C3 = set(2)  #Com um argumento 

#Solução pra isso para poder usar o set() inves de '{}'(um par de chaves)
C3 = set( [4, 67, 59, 2] )  #colocar uma lista dos varios elementos

OU

C3 = set( (4, 67, 59, 2) ) #colocar uma tupla dos varios eementos que fazem parte do conjunto

```

O que caracteriza um conjunto são além do “{}”(par de chaves), ele também não pode ter números repetidos, pois se tiver 2 e quisermos ver o que tem nesse conjunto ele só apresentará somente um numero mesmo que o numero esteja repetido duas vezes.

```c
C = {15, 4, 56, 7, 58, 69, 4}

print(C)

#Resposta do print
{15, 4, 56, 7, 58, 69}
```

  - 2ª Modo - Criar um conjunto sem conteúdo, ou seja, um conjunto vazio

```c
C2 = set()
type(C2)

#Resposta do type
<classe 'set'>

#Se colocar assim, não vai dar certo
C3 = {}  #Pois assim não estamos criando um conjunto e sim outro tipo de objeto
type(C3)

#Resposta do type
<classe 'dict> classe dicionario
```

**Resumo**: Formas de criar conjuntos

```c
#Conjunto com Dados
C1 = {1, 2, 3, 4}

#Conjunto com Dados com Tuplas ou lista
C2 = set( (1, 2, 3, 4) ) #Tupla
C2 = set( [1, 2, 3, 4] ) #Lista

#Conjunto Vazio (Sem dados)
C3 = set()
```

**Conjunto de outros tipo de elementos**

```c
texto = 'qualquer texto'

C1 = set(texto)

#Resposta de C1
{ 'r', 'e', 'l', 'x', 'q','u', 't', '', 'o'}  #O conjunto criado é uma coleção de caracteres que são oriundos do texto que foi usado para construção,isso sempre repetição de letras

```

```c
tupla = (26, 73, 41)

C2 = set(tupla)

#Resposta de C2
{73, 26, 41}
```

```c
lista = [ 32, 34]

C3 = set(lista)

#Resposta de C3
{32, 34}
```

---

- **Hash** é uma forma de criar uma identificação para um objeto, baseado no conteudo do objeto

```c
S1 = 'abcd'
hash(S1)    #o Hash aqui é um algortimo que a partir do conteudo acima ele irá criar um numero inteiro

#Resposta do Hash
-65849895614

#Se colocarmos o valor emoutro objeto a resposta de numerario será a mesma
```

**Nota:** Todo o objeto Mutável, não tem hash, pois não tem como calcular o hash de objetos mutáveis, e todo objeto imutável tem hash.

- É a existência do hash que define se um elemento pode pertencer a um conjunto.
- O hash de um numero inteiro é o proprio numero, mas um monte de numero tem um hash diferente
- Sabes a parte de que um set(), não parece 2 números iguais isso é por causa, ou pq que um conjunto não pode conter um inteiro e um float de mesma magnitude, é por causa do calculo do numero hash, que é o que determina se um objeto estará no conjunto ou não.

---

**Metodos da Classe set**

- add - para adicionar um elemento dentro de um conjunto, é tipo o append. Quando você coloca a ordem colocada lá é aleatoria.

```c
c - set()

c.add(32)
c.add(76)

print(c)

#Resposta
{76, 32}
```

- clear - para limpar um determinado conjunto e ai ele fica vazio. c.clear()
- copy - se quisermos um clone ou copia de um conjunto. **c.copy(),** o ID dele é sempre diferente do que foi copiado.
- difference - usado para quando temos 2 conjunto nos mostrar os elementos que se assemelham em cada conjunto e apresentar para nós

```c
c1 = {26, 32, 45, 58, 63}
c2 = {19, 34, 58, 67, 82}

c1.difference(c2)
#Resposta
{32, 26, 45, 63}

Se colocarmos o _update, ele somente atualiza o argumento
c1.difference_update(c2)
```

- discard - ele remove um elemento, se ele não estiver no conjunto e nem tira mas se tiver ele tira. **c1.discard(32)**
- intersection - ele simplesmente retorna um conjunto novo que pode ser atribuído a um novo identificador, sendo o resultado as parte iguais dos dois conjuntos. **c1.intersection(c2)**
- isdisjoint - ele mostra se, tendo em conta os conjunto se sã disjuntos ou não, iguais ou diferentes. **c1.isdisjoint.(c2) - ele retorna Booleano**
- subset - ele é verdadeiro quando c1 for subconjunto de c2, fazendo uma verificação se todos os elementos em c1 também estão em c2. **c1.subset(c2) - ele retorna   Booleano**
- issurperset - ele retorna verdadeiro quando o conjunto c1 é um superconjunto de c2,ou seja todos os elementos de c2 estão contidos em c1 ou vai retornar verdadeiro quando c1 tem todos os elementos em c2. **c1.superset(c2) - ele retorna também Booleano**
- pop - ele remove algum elemento do conjunto, ele mesmo escolhe e remove e tem de atribuir a um objeto pra sabermos quem foi removido

```c
c1 = {26, 32, 45, 58, 63}
a = c1.pop()  #em 'a' estamos armazenar o que foi removdo do conjunto c1

print(a)
#Resposta
32

print(c1)
#Resposta
{26, 45, 58, 63}
```

- remove -ele remove um elemento do conjunto. **c1.remove()**

```c
NOTA: para podermos por vezes ver se o elemento esta contindo emum conjunto,para isso usamos o operador 'IN'

EX:

26 in c1
#resposta
True

99 in c1
#resposta
False

Temos de saber o elemento se esta lá antes de remove-lo
```

- union - usados para podermos unir ou juntar 2 conjuntos sem repetições de elementos. **c1.union(c2)**

---

Classe dict - Muito parecido com uma lista, a diferença é que a identificação de um elemento dentro d uma dicionário não será feito por um índice numérico como em uma lista(Ex na imagem),mas sim por uma valor chave que nós escolhemos o que será (pode ser um texto, numero, pode ser qualquer objeto de classe que tenha Hash, ou seja, que seja imutável(tuplas, etc)).

![image.png](attachment:009e535c-9bc8-454c-9189-e15843cc8d3a:image.png)

```c
#Para criar ele tem de ser assim

UF = {'SP': 'São Paulo', 'RJ': 'Rio de Janeiro'}

type(UF)
#Resposta
<classe 'dict'>

# Se for vazio

UF ={}

#Mas se tiver de colocar elementos nele só fazer assim

UF['SP'] = 'São Paulo'
UF['RJ'] = 'Rio de Janeiro'

print(UF)
#Resposta
UF = {'SP': 'São Paulo', 'RJ': 'Rio de Janeiro'}

#Se nós colocarmos o mesmo indice duas vezes para 2 elementos diferentes ao adicionar eles
#Ele irá adicionar o indice ao ultimo colocado, ou seja, altera e é assim que se altera o indice me um dict Ex

UF = {}
UF['a'] = 120

print(UF)
#Resposta
{'a': 120}

UF['a'] = 250

print(UF)
#Resposta
{'a': 250} #assim o elemento foi alterado,qundoa fazemos uma atribuição a um elemento do dict

```

**Nele podemos fazer determinadas operações usando os elementos**

```c

UF['a'] = 90
UF['b'] = 521

x = UF[a] + UF[b]

print(x)
#Resposta
611

#E podemos fazer outras também identificando o indice, sempre para usar o seu valor

x = UF[a] + 100

print(x)
#Resposta
190
```