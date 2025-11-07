# Exercício 6.19 - Coleções

## Enunciado

Faça um programa que declare uma lista de 10 números e mostre os 5 primeiros elementos e os 5 últimos elementos da lista separadamente.

## Solução

```python
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("5 primeiros elementos:", lista[:5])
print("5 últimos elementos:", lista[-5:])
```

## Explicação

Nesta solução, temos uma lista de 10 números. Usamos a técnica de fatiamento de lista para obter os 5 primeiros e os 5 últimos elementos da lista. Ao fim, imprimimos ambos os subconjuntos de elementos.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
