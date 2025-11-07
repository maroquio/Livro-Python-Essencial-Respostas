# Exercício 5.2 - Funções

## Enunciado

Crie uma função que tenha um número inteiro como parâmetro e retorne `True` se o número for par e `False` se o número for ímpar. Em seguida, crie uma chamada para essa função passando argumentos para os parâmetros e mostrando o resultado na tela.

## Solução

```python
def eh_par(num):
    return num % 2 == 0

resultado = eh_par(7)
print(resultado)
```

## Explicação

Neste código, a função `eh_par()` é definida com um parâmetro, `num`. Esta função retorna `True` se o número for par (ou seja, se o resto da divisão de `num` por 2 for igual a 0) e `False` caso contrário. Chamamos a função `eh_par()` passando 7 como argumento e armazenamos o resultado retornado em `resultado`. Em seguida, imprimimos `resultado`.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
