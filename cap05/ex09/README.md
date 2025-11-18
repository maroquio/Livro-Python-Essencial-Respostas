# Exercício 5.9 - Funções

## Enunciado

Você é um sommelier em um restaurante de alto padrão e tem uma longa lista de vinhos, cada um com um preço diferente. O seu gerente lhe deu uma tarefa: encontrar os vinhos mais caros da lista para uma degustação especial. Para isso, você vai precisar de uma função que possa filtrar os vinhos por preço. Como a lista de vinhos está sempre mudando, essa função precisa ser flexível e fácil de alterar. Escreva um programa que crie uma lista de vinhos, onde cada vinho é representado por um dicionário com o nome e o preço do vinho. Em seguida, use uma função lambda para criar uma nova lista contendo apenas os vinhos que custam mais de 50 reais. Imprima esta nova lista de vinhos caros.

## Solução

```python
vinhos = [
    {"nome": "Vinho A", "preco": 45},
    {"nome": "Vinho B", "preco": 80},
    {"nome": "Vinho C", "preco": 30},
    {"nome": "Vinho D", "preco": 60},
    {"nome": "Vinho E", "preco": 120}
]

vinhos_caros = list(filter(lambda vinho: vinho["preco"] > 50, vinhos))
print(vinhos_caros)
```

## Explicação

A lista `vinhos` é composta por dicionários, onde cada dicionário representa um vinho, contendo um campo para o nome do vinho e um campo para o preço do vinho. Para filtrar os vinhos que custam mais de 50 reais, usamos a função `filter`, que aplica uma função a cada elemento da lista e retorna uma nova lista com os elementos para os quais a função retorna verdadeiro. A função que usamos é uma função lambda que verifica se o preço do vinho é maior que 50. A função `filter` retorna um iterador, então usamos a função `list` para converter o iterador em uma lista. O resultado é uma nova lista `vinhos_caros` que contém apenas os vinhos que custam mais de 50 reais. Finalmente, imprimimos a lista `vinhos_caros`.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
