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