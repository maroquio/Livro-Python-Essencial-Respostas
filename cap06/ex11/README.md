# Exercício 6.11 - Coleções

## Enunciado

Faça um programa que peça ao usuário para digitar uma lista de números e que, em seguida, use filtragem (`filter`) para retornar uma nova lista apenas com os números pares.

## Solução

```python
numeros = list(map(int, input("Digite uma lista de números separados por vírgula: ").split(",")))
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)
```

## Explicação

Nesta solução, pedimos ao usuário para digitar uma lista de números separados por vírgulas e convertemos a *string* de entrada em uma lista de números inteiros com a função `map()`. Utilizamos a função `filter()` para filtrar apenas os números pares da lista, usando uma função lambda para verificar se o módulo de um número por 2 é igual a zero. Ao final, convertemos o objeto `filter` resultante em uma lista e a imprimimos.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
