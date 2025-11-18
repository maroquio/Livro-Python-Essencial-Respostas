# Exercício 6.5 - Coleções

## Enunciado

Faça um programa que crie um dicionário com nomes e notas de alunos, ambos digitados pelo usuário, usando os nomes dos alunos como chave e as notas como valor. Em seguida, use *Dict Comprehension* para criar um dicionário com os alunos com nota igual ou superior a 7.

## Solução

```python
nomes_notas = {"Pedro": 6, "Maria": 9, "João": 8, "Ana": 7}
aprovados = {nome: nota for nome, nota in nomes_notas.items() if nota >= 7}
```

## Explicação

Nesse código, primeiro definimos um dicionário chamado `nomes_notas` com nomes de alunos como chaves e suas notas como valores. Então, usamos *dict comprehension* para criar um novo dicionário `aprovados`. No novo dicionário, incluímos apenas alunos cuja nota é maior ou igual a 7. Vale lembrar que a estrutura *dict comprehension* é semelhante à *list comprehension*, mas usamos chaves e valores em vez de itens individuais.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
