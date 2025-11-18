# Exercício 6.30 - Coleções

## Enunciado

Crie um *generator* que simule um fluxo de dados capturados de um sensor. O sensor gera uma leitura (um número aleatório entre 0 e 100) a cada iteração. Use o *generator* para imitar a leitura do sensor 10 vezes.

## Solução

```python
import random

def leitura_sensor():
    while True:
        yield random.randint(0, 100)

generator = leitura_sensor()
for i in range(10):
    print(next(generator))
```

## Explicação

O *generator* `leitura_sensor` gera uma sequência de números aleatórios entre 0 e 100, simulando as leituras de um sensor. Podemos usar a função `next()` para ler o próximo valor do sensor. Ao fim, usamos a função *generator* `leitura_sensor()` para obter 10 leituras do sensor simulado.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
