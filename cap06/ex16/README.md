# Exercício 6.16 - Coleções

## Enunciado

Faça um programa que declare uma lista de 10 números inteiros e inverta a ordem dos elementos de índices pares. Ao fim, mostre a lista resultante.

## Solução

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Cria uma lista com os valores de índice par
nums_indices_pares = [numeros[i] for i in range(0, len(numeros), 2)]

# Inverte a lista de valores obtida
nums_indices_pares.reverse()

# Substitui os valores de índice par da lista original pelo valor correspondente da lista invertida
for i in range(0, len(numeros), 2):
    numeros[i] = nums_indices_pares.pop(0)

print(numeros)
# Saída: [9, 2, 7, 4, 5, 6, 3, 8, 1, 10]
```

## Explicação

Neste código, primeiro criamos uma lista chamada `numeros` contendo 10 números inteiros. Em seguida, usamos *list comprehension* para criar uma nova lista, `indices_pares`, contendo apenas os elementos da lista `numeros` que estão em posições pares (índice 0, 2, 4 etc.). O método `range(0, len(numeros), 2)` é usado para gerar os índices pares. Depois, usamos o método `reverse()` para inverter a ordem dos elementos em `nums_indices_pares`. Em seguida, percorremos novamente os índices pares da lista `numeros` usando um laço `for` e o mesmo método `range()` que usamos antes. Dentro desse laço, substituímos o elemento na posição par da lista `numeros` pelo primeiro elemento de `nums_indices_pares` (que está na ordem inversa) e depois removemos esse elemento de `nums_indices_pares` usando o método `pop(0)`. Por fim, imprimimos a lista `numeros`, que agora tem a ordem dos elementos de índices pares invertida.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
