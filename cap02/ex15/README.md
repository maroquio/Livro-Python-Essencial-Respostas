# Exercício 2.15 - Estruturas Condicionais

## Enunciado

Crie um programa que peça ao usuário para digitar uma palavra. O programa deve então indicar se a palavra inserida começa com uma vogal ou uma consoante.

## Solução

```python
palavra = input("Insira uma palavra: ")
primeira_letra = palavra[0].lower()
if primeira_letra in 'aeiou':
    print(f"A palavra '{palavra}' começa com uma vogal.")
else:
    print(f"A palavra '{palavra}' começa com uma consoante.")
```

## Explicação

O programa solicita uma palavra ao usuário, depois obtém a primeira letra da palavra (`palavra[0]`) e a converte em minúsculas (`lower()`), para assegurar que a comparação seja *case-insensitive*. Se essa primeira letra estiver no conjunto de caracteres 'aeiou' (ou seja, for uma vogal), o programa informará que a palavra começa com uma vogal. Caso contrário, o programa informará que a palavra começa com uma consoante.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
