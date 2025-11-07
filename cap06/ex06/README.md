# Exercício 6.6 - Coleções

## Enunciado

Faça um programa que use *Dict Comprehension* para criar um dicionário com as raízes quadradas dos números de 1 a 10. Utilize os números como chave e as raízes quadradas como valor.

## Solução

```python
raizes_quadradas = {n: n**0.5 for n in range(1, 11)}
```

## Explicação

Nesse código, usamos a *dict comprehension* para gerar um dicionário chamado `raizes_quadradas`. As chaves são números de 1 a 10 e os valores são as raízes quadradas desses números. A expressão `n**0.5` calcula a raiz quadrada de `n`. A função `math.sqrt()` também poderia ter sido usada para se obter a raiz quadrada.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
