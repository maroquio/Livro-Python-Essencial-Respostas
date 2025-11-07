# Exercício 5.10 - Funções

## Enunciado

Crie uma função de ordem superior chamada `transformarLista` que aceite uma lista de números inteiros e uma função como parâmetros. Aplique a função do parâmetro a cada um dos elementos da lista passada como argumento, retornando uma nova lista de mesmo tamanho, porém, com os elementos transformados. Agora crie uma função chamada `porExtenso` que receba um número inteiro entre 0 e 9 como argumento e retorne seu nome por extenso. Para concluir, chame a função `transformarLista` passando [1, 2, 3, 4, 5] como primeiro argumento e a função `porExtenso` como segundo argumento, mostrando a lista resultante.

## Solução

```python
def transformarLista(lista, funcao):
    return [funcao(x) for x in lista]

def porExtenso(num):
    numeros = {
        0: "zero",
        1: "um",
        2: "dois",
        3: "três",
        4: "quatro",
        5: "cinco",
        6: "seis",
        7: "sete",
        8: "oito",
        9: "nove"
    }
    return numeros.get(num)

lista_original = [1, 2, 3, 4, 5]
lista_transformada = transformarLista(lista_original, porExtenso)
print(lista_transformada)
```

## Explicação

A função `transformarLista` é uma função de ordem superior que recebe uma lista e uma função como argumentos. Essa função retorna uma nova lista que é o resultado de aplicar a função fornecida a cada elemento da lista original. Isso é feito usando uma compreensão de lista.

A função `porExtenso` recebe um número inteiro entre 0 e 9 e retorna o nome desse número por extenso. Ela usa um dicionário para mapear números a seus nomes por extenso.

Para usar essas funções, criamos uma `lista_original` com os números de 1 a 5. Em seguida, chamamos a função `transformarLista`, passando a `lista_original` e a função `porExtenso` como argumentos. O resultado é uma nova lista `lista_transformada` que contém os nomes por extenso dos números da lista original. Por fim, imprimimos a `lista_transformada`.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
