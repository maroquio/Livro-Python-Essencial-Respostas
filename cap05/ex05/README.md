# Exercício 5.5 - Funções

## Enunciado

Crie uma função que defina uma variável `x` dentro da função e imprima o valor de `x` na tela. Em seguida, fora da função, crie uma linha de código para imprimir o valor de `x` e analise o erro que será gerado ao tentar executar o programa.

## Solução

```python
def funcao():
    x = 10
    print(x)

funcao()
print(x)
```

## Explicação

A função `funcao()` define uma variável local `x` e a imprime. Em seguida, tentamos imprimir `x` fora da função. No entanto, isso leva a um erro porque `x` é uma variável local dentro da função `funcao()` e não está definida fora da função.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
