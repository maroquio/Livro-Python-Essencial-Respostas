# Exercício 3.19 - Estruturas de Repetição

## Enunciado

Crie um programa que verifique se uma palavra digitada pelo usuário é um palíndromo. Se for, imprimir, ao final, "A palavra é um palíndromo". Se não for, imprimir "A palavra não é um palíndromo".

## Solução

```python
palavra = input("Digite uma palavra: ")
palavra_invertida = ""

for i in range(len(palavra) - 1, -1, -1):
    palavra_invertida += palavra[i]

if palavra == palavra_invertida:
    print("A palavra é um palíndromo")
else:
    print("A palavra não é um palíndromo")
```

## Explicação

Neste programa, a abordagem é similar à solução anterior, mas sem usar a função `reversed()`. Primeiro, o programa lê a palavra do usuário e inicia uma *string* vazia `palavra_invertida`. A função `range()` é utilizada para gerar uma sequência de índices que começa no último índice da palavra (ou seja, `len(palavra) - 1`) e vai até o primeiro índice (ou seja, 0, pois o segundo argumento, que é o limite, vale `-1`), decrementando 1 a cada iteração (isso é indicado pelo terceiro argumento `-1` na função `range()`). O laço `for` percorre esta sequência de índices. Para cada índice, a letra correspondente da palavra é adicionada ao final da `palavra_invertida`. Finalmente, o programa compara a palavra original e a `palavra_invertida`. Se são iguais, o programa imprime "A palavra é um palíndromo". Caso contrário, imprime "A palavra não é um palíndromo".

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
