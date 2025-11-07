# Exercício 5.7 - Funções

## Enunciado

Escreva uma função recursiva chamada `contagemRegressiva` que aceite um número inteiro como entrada e imprima todos os números de *n* até 0, seguidos por "Contagem regressiva finalizada!". Por exemplo, a chamada `contagemRegressiva(5)` deve imprimir 5, 4, 3, 2, 1, 0, "Contagem regressiva finalizada!".

## Solução

```python
def contagemRegressiva(n):
    if n >= 0:
        print(n)
        contagemRegressiva(n-1)
    else:
        print("Contagem regressiva finalizada!")

contagemRegressiva(5)
```

## Explicação

A função `contagemRegressiva()` é uma função recursiva que imprime um número `n` e então chama a si mesma com o argumento `n-1`, continuando até que `n` seja menor que 0. Quando `n` é menor que 0, a função imprime a frase "Contagem regressiva finalizada!".

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
