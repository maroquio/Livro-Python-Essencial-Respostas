# Exercício 6.26 - Coleções

## Enunciado

Crie um *generator* que produza uma sequência infinita de números inteiros, começando por 1. Em seguida, faça um laço para imprimir os primeiros 10 números dessa sequência.

## Solução

```python
def sequencia_infinita():
    num = 1
    while True:
        yield num
        num += 1

generator = sequencia_infinita()
for i in range(10):
    print(next(generator))
```

## Explicação

Esta função define um *generator* que começa a partir do número 1 e incrementa este número a cada passo. Cada vez que a função `next()` é chamada no *generator*, a execução da função recomeça de onde parou na última vez que o `yield` foi encontrado, tornando possível gerar uma sequência infinita de números inteiros.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
