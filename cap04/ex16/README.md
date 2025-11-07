# Exercício 4.16 - Números, Textos, Datas e Horas

## Enunciado

Faça um programa que crie um objeto `datetime` que represente o instante atual.

## Solução

```python
from datetime import datetime as dt

data_hora_atual = dt.now()
print(data_hora_atual)
```

## Explicação

Neste código, importamos o módulo `datetime` e criamos *alias* para ele chamado `dt`. Em seguida, criamos um objeto `datetime` que representa a data e hora atuais usando o método `now()`. Por fim, a data e a hora atuais são impressas.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
