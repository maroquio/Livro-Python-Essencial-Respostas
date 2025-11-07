# Exercício 9.2 - Tratamento de Exceções

## Enunciado

Crie uma função que receba uma lista de números e retorne a média aritmética deles. Trate exceções caso a lista seja vazia ou contenha valores não numéricos.

## Solução

```python
def calcular_media(lista):
    try:
        return sum(lista) / len(lista)
    except ZeroDivisionError:
        print("Erro: Não é possível calcular a média de uma lista vazia.")
    except TypeError:
        print("Erro: Todos os elementos da lista devem ser numéricos.")

lista = [1, 2, 3, 4, 5]
print(calcular_media(lista))
```

## Explicação

A função `calcular_media` recebe uma lista de números e retorna a média aritmética deles. Ela tenta somar todos os elementos da lista (usando a função `sum`) e divide pelo número total de elementos na lista (obtido através da função `len`). Se a lista estiver vazia, a divisão por zero causará uma `ZeroDivisionError`, que é capturada e tratada com uma mensagem de erro apropriada. Se a lista contiver elementos não numéricos, a soma desses elementos lançará uma `TypeError`, que também é capturada e tratada com uma mensagem de erro apropriada.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
