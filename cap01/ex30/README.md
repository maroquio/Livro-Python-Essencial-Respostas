# Exercício 1.30 - Fundamentos da Linguagem

## Enunciado

Crie um programa que tenha dois conjuntos de 5 números quaisquer e combine-os usando as operações de união, interseção e diferença, apresentando os resultados de cada operação.

## Solução

```python
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

uniao = conjunto1.union(conjunto2)
intersecao = conjunto1.intersection(conjunto2)
diferenca1 = conjunto1.difference(conjunto2)
diferenca2 = conjunto2.difference(conjunto1)

print("União dos conjuntos:", uniao)
print("Interseção dos conjuntos:", intersecao)
print("Diferença entre conjunto1 e conjunto2:", diferenca1)
print("Diferença entre conjunto2 e conjunto1:", diferenca2)
```

## Explicação

Neste código, criamos dois conjuntos, `conjunto1` e `conjunto2`, cada um contendo 5 números quaisquer. Em seguida, utilizamos os métodos `union()`, `intersection()` e `difference()` para realizar as operações de união, interseção e diferença entre os conjuntos, armazenando os resultados nas variáveis `uniao`, `intersecao`, `diferenca1` e `diferenca2`, respectivamente. Por fim, imprimimos os resultados de cada operação.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
