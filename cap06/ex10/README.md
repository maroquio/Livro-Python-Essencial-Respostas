# Exercício 6.10 - Coleções

## Enunciado

Faça um programa que peça ao usuário para digitar uma lista de palavras e que, em seguida, use mapeamento (`map`) para retornar uma nova lista com os comprimentos de cada palavra.

## Solução

```python
palavras = input("Digite uma lista de palavras separadas por vírgula: ").split(",")
comprimentos = list(map(len, palavras))
print(comprimentos)
```

## Explicação

Nesta solução, pedimos ao usuário para digitar uma lista de palavras separadas por vírgulas. Utilizamos a função `map()` para aplicar a função `len` a cada palavra na lista, retornando um objeto `map` com os comprimentos de cada palavra. Ao final, convertemos esse objeto `map` em uma lista e a imprimimos.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
