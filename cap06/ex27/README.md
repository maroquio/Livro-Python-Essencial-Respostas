# Exercício 6.27 - Coleções

## Enunciado

Crie um *generator* que produza os números da sequência Fibonacci. Use este *generator* para imprimir os primeiros 20 números da sequência.

## Solução

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

generator = fibonacci()
for i in range(20):
    print(next(generator))
```

## Explicação

Aqui temos uma função *generator* que produz a sequência de Fibonacci. O uso de `yield` permite que os dois últimos números da sequência sejam armazenados e usados para calcular o próximo número toda vez que a função `next()` é chamada no *generator*.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
