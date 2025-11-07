# Exercício 6.7 - Coleções

## Enunciado

Faça um programa que crie um dicionário com nomes e notas de alunos, ambos digitados pelo usuário, usando os nomes dos alunos como chave e as notas como valor. Em seguida, use *Dict Comprehension* para criar um dicionário com os alunos e suas notas arredondadas para o número inteiro mais próximo da nota do aluno.

## Solução

```python
nomes_notas = {"Pedro": 6.5, "Maria": 8.7, "João": 8.3, "Ana": 7.2}
notas_arredondadas = {nome: round(nota) for nome, nota in nomes_notas.items()}
```

## Explicação

Nesse código, definimos um dicionário chamado `nomes_notas` com nomes de alunos como chaves e suas notas como valores. Então, usamos *dict comprehension* para criar um novo dicionário `notas_arredondadas`, no qual arredondamos cada nota para o número inteiro mais próximo usando a função `round()`.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
