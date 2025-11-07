# Exercício 2.23 - Estruturas Condicionais

## Enunciado

Desenvolva um "Tradutor de Emoções" que peça ao usuário para inserir uma emoção (feliz, triste, nervoso etc.). Utilize a estrutura `match..case` para imprimir um emoji correspondente a essa emoção. Por exemplo, imprimir :) para feliz, :( para triste etc.

## Solução

```python
emocao = input("Insira uma emoção (feliz, triste, nervoso): ").lower()

match emocao:
    case "feliz":
        print(":)")
    case "triste":
        print(":(")
    case "nervoso":
        print(":/")
    case _:
        print("Emoção não reconhecida")
```

## Explicação

Este programa é um "Tradutor de Emoções" que usa a estrutura `match` para imprimir um emoji correspondente à emoção inserida pelo usuário. Os emojis são selecionados com base na emoção inserida e um caso padrão é incluído para lidar com entradas não reconhecidas.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
