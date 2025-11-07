# Exercício 6.14 - Coleções

## Enunciado

Faça um programa que declare duas listas de mesmo tamanho, uma com 3 nomes de alunos e outra com 3 notas. Em seguida, usando a função `zip` e *List Comprehension*, retorne uma lista com as tuplas (nome, nota) em ordem decrescente de nota.

## Solução

```python
nomes = ["Ana", "João", "Carlos", "Pedro"]
notas = [8.5, 9.0, 7.0, 8.0]

lista_notas = sorted([(nome, nota) for nome, nota in zip(nomes, notas)], key=lambda x: x[1], reverse=True)
```

## Explicação

Nesta solução, temos duas listas: `nomes`, que contém os nomes dos alunos, e `notas`, que contém as notas correspondentes. Usamos a função `zip()` para agrupar os elementos correspondentes de `nomes` e `notas`. Em seguida, usamos a função `sorted()` para ordenar a lista de tuplas em ordem decrescente de nota (índice 1 das tuplas), que é o que `lambda x: x[1]` especifica. O parâmetro `reverse=True` garante que a ordenação seja decrescente.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
