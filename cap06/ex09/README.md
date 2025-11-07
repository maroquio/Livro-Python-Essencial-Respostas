# Exercício 6.9 - Coleções

## Enunciado

Faça um programa que peça ao usuário para digitar uma lista de nomes e que, em seguida, use mapeamento (`map`) para retornar uma nova lista com os nomes em caixa alta.

## Solução

```python
nomes = input("Digite uma lista de nomes separados por vírgula: ").split(",")
nomes_upper = list(map(str.upper, nomes))
print(nomes_upper)
```

## Explicação

Nesta solução, pedimos ao usuário para digitar uma lista de nomes separados por vírgulas. Em seguida, usamos a função `input().split(",")` para converter a *string* de entrada em uma lista de nomes. Utilizamos a função `map()` para aplicar a função `str.upper` a cada nome na lista, retornando um objeto `map`. Por fim, convertemos esse objeto `map` em uma lista e a imprimimos.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
