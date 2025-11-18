# Exercício 6.12 - Coleções

## Enunciado

Faça um programa com duas listas contendo 3 valores cada, uma com chaves (*string*) e outra com os valores (`int`), e retorne um dicionário criado a partir destas duas listas.

## Solução

```python
chaves = ["chave1", "chave2", "chave3"]
valores = [1, 2, 3]

dicionario = {chaves[i]: valores[i] for i in range(len(chaves))}
print(dicionario)
```

## Explicação

Nesta solução, temos duas listas de mesmo tamanho: uma lista de chaves e uma lista de valores. Utilizamos *dict comprehension* para criar um dicionário, onde cada chave é mapeada para o valor correspondente na lista de valores. Para percorrer as duas listas ao mesmo tempo, usamos a função `range()` com o comprimento das listas (que são do mesmo tamanho). Ao fim, imprimimos o dicionário resultante.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
