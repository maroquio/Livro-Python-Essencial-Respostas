# Exercício 4.17 - Números, Textos, Datas e Horas

## Enunciado

Faça um programa que crie um objeto `date` que represente a data atual.

## Solução

```python
from datetime import datetime as dt

data_atual = dt.now().date()
print(data_atual)
```

## Explicação

Neste código, importamos o módulo `datetime` e criamos um objeto `date` que representa a data atual usando o método `date.today()`. Por fim, a data atual é impressa.

---
*Livro: Python Essencial: Para Programadores - Ricardo Maroquio*
