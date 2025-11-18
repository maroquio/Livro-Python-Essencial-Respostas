# Exercício 2.6 - Estruturas Condicionais

## Enunciado

Crie um programa que verifique se um texto digitado pelo usuário é um palíndromo ou não (use `texto[::-1]` para obter o texto invertido).

## Solução

```python
texto = input("Digite um texto: ").replace(" ", "").lower()
texto_invertido = texto[::-1]

if texto == texto_invertido:
    print("O texto é um palíndromo.")
else:
    print("O texto não é um palíndromo.")
```

## Explicação

Neste código, solicitamos ao usuário que digite um texto e armazenamos o valor na variável `texto`. Em seguida, removemos os espaços em branco usando o método `replace()` e convertemos o texto para minúsculas usando o método `lower()`. Obtemos o texto invertido usando a técnica de fatiamento `texto[::-1]` e armazenamos o resultado na variável `texto_invertido`. Verificamos se o texto é um palíndromo comparando `texto` e `texto_invertido`. Se forem iguais, o texto é um palíndromo; caso contrário, não é. Por fim, imprimimos o resultado.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
