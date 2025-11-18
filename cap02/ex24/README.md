# Exercício 2.24 - Estruturas Condicionais

## Enunciado

Escreva um programa que peça ao usuário para inserir uma faixa etária e, em seguida, utilize a estrutura `match..case` para sugerir um filme adequado para essa idade. Você pode categorizar as faixas etárias e sugerir diferentes tipos de filmes para cada categoria, como filmes infantis para crianças, ação para adolescentes, drama para adultos etc.

## Solução

```python
faixa = input("Insira sua faixa etária (criança, adolescente, adulto): ").lower()

match faixa:
    case "criança":
        print("Sugerido: Filme infantil")
    case "adolescente":
        print("Sugerido: Filme de ação")
    case "adulto":
        print("Sugerido: Filme de drama")
    case _:
        print("Faixa etária não reconhecida")
```

## Explicação

Nesta solução, pedimos ao usuário para inserir uma faixa etária e utilizamos a estrutura `match` para sugerir um filme adequado. Os filmes são sugeridos com base na faixa etária inserida, e um caso padrão é incluído para lidar com entradas não reconhecidas.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
