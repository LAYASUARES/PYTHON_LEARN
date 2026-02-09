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

Condicional if que é escrito em uma unica linha mais conhecido como **If inline**

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

Nota: nessa construção inline o else é obrigatório colocar e não usamos o “:”, ou seja, If inline podemos usar desde que seja completo e somente quando tiver um único comando na parte do else e na parte do if

---

